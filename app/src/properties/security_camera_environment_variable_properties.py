import logging

from properties.security_camera_properties import SecurityCameraProperties
from os import environ

LOGGER = logging.getLogger(__name__)


class SecurityCameraEnvironmentVariableProperties(SecurityCameraProperties):
    def __init__(self):
        super().__init__()
        LOGGER.info("Environment variable security camera properties used.")
        self.set_rabbitmq_properties()

    def set_rabbitmq_host_ip(self):
        self._rabbitmq_host_ip = environ["RABBITMQ_HOST_IP"]

    def set_security_config_exchange_name(self):
        self._security_config_exchange_name = environ["SECURITY_CONFIG_EXCHANGE_NAME"]

    def set_security_config_queue_name(self):
        self._security_config_queue_name = environ["SECURITY_CONFIG_QUEUE_NAME"]

    def set_logging_property_file(self):
        self._logging_property_file = environ["LOGGING_PROPERTY_FILE"]

    def set_pir_sensor_pin(self):
        self._pir_sensor_pin = environ["PIR_SENSOR_PIN"]

    def set_pir_num_readings(self):
        self._pir_num_readings = environ["PIR_NUM_READINGS"]

    def set_pir_detections_per_second(self):
        self._pir_detections_per_second = environ["PIR_DETECTIONS_PER_SECOND"]

    def set_pir_threshold(self):
        self._pir_threshold = environ["PIR_THRESHOLD"]

    def set_led_pin(self):
        self._led_pin = environ["LED_PIN"]

    def set_security_micro_service_host_ip(self):
        self._security_micro_service_host_ip = environ["SECURITY_MICRO_SERVICE_HOST_IP"]

    def set_security_micro_service_host_port(self):
        self._security_micro_service_host_port = environ["SECURITY_MICRO_SERVICE_HOST_PORT"]

    def set_security_micro_service_context_path(self):
        self._security_micro_service_context_path = environ["SECURITY_MICRO_SERVICE_CONTEXT_PATH"]

    def set_security_camera_microservice_capture_directory(self):
        self._security_camera_microservice_capture_directory = environ["SECURITY_CAMERA_MICROSERVICE_CAPTURE_DIRECTORY"]
