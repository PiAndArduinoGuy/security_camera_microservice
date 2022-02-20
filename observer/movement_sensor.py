import base64
import logging
from threading import Thread

from gpiozero import MotionSensor, LED
from picamera import PiCamera

from observer_design_pattern.observer import Observer
from observer_design_pattern.subject import Subject
from properties.security_camera_properties import SecurityCameraProperties
from web.security_micro_service_web_client import SecurityMicroServiceWebClient

LOGGER = logging.getLogger(__name__)


class MovementSensor(Observer):
    def __init__(self,
                 subject: Subject,
                 security_camera_properties: SecurityCameraProperties,
                 security_micro_service_web_client: SecurityMicroServiceWebClient):
        super().__init__(subject)
        self.subject.add_observer(self)
        self._pir_sensor = MotionSensor(pin=security_camera_properties.get_pir_sensor_pin(),
                                        queue_len=security_camera_properties.get_pir_num_readings(),
                                        sample_rate=security_camera_properties.get_pir_detections_per_second(),
                                        threshold=security_camera_properties.get_pir_threshold())
        self._led = LED(security_camera_properties.get_led_pin())
        self._camera = PiCamera()
        self._is_armed = False
        self._has_active_thread = False
        self._security_micro_service_web_client = security_micro_service_web_client
        self.security_camera_microservice_capture_directory = \
            security_camera_properties.get_security_camera_microservice_capture_directory()

    def update(self):
        security_config = self.subject.get_state()
        security_state = security_config["securityState"]
        if security_state == 'ARMED':
            LOGGER.info("Security state is ARMED, motion detecting will be enabled.")
            self._is_armed = True
            if not self._has_active_thread:
                self._has_active_thread = True
                perform_detection_thread = Thread(name="perform_detection_thread",
                                                  target=self.perform_detection)
                perform_detection_thread.start()
            else:
                LOGGER.info("There is currently an active thread, a new one will not be created.")
        elif security_state == 'DISARMED':
            LOGGER.info("Security state is DISARMED, motion detecting will be disabled.")
            self._is_armed = False

    def perform_detection(self):
        def get_base64_encoded_image():
            with open(file=f"{self.security_camera_microservice_capture_directory}/new_capture.jpeg", mode="rb") as new_capture_file:
                new_capture_binary_data = new_capture_file.read()
                return base64.b64encode(new_capture_binary_data)

        LOGGER.info("Motion detection started.")
        while self._is_armed:
            self._pir_sensor.wait_for_motion()
            LOGGER.info("Motion detected.")

            self._capture_image()
            self._trigger_visual_indicator()
            self._security_micro_service_web_client.send_image_for_security_check(get_base64_encoded_image())

        LOGGER.info("Motion detection stopped.")
        self._has_active_thread = False

    def _capture_image(self):
        LOGGER.info("Capturing image.")
        self._camera.capture(f"{self.security_camera_microservice_capture_directory}/new_capture.jpeg")

    def _trigger_visual_indicator(self):
        LOGGER.info("Turn LED on.")
        self._led.on()
        self._pir_sensor.wait_for_no_motion()  # keep the led on while motion detected
        LOGGER.info("Turn LED off.")
        self._led.off()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing PIR MotionSensor, LED and camera resources.")
        self._pir_sensor.close()
        self._led.off()
        self._led.close()
        self._camera.close()
        print("Connections closed.")
