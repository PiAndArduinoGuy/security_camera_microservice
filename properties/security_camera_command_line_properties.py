import argparse

from properties.security_camera_properties import SecurityCameraProperties


class SecurityCameraCommandLineProperties(SecurityCameraProperties):
    def __init__(self):
        super().__init__()
        parser = argparse.ArgumentParser()
        parser.add_argument("--rabbitmq_host_ip", required=True)
        parser.add_argument("--security_config_queue_name", required=True)
        parser.add_argument("--security_config_exchange_name", required=True)
        parser.add_argument("--logging_file_location", required=True)
        parser.add_argument("--security_micro_service_host_ip", required=True)
        parser.add_argument("--security_micro_service_host_port", required=True)
        parser.add_argument("--pir_sensor_pin")
        parser.add_argument("--pir_num_readings")
        parser.add_argument("--pir_detections_per_second")
        parser.add_argument("--pir_threshold")
        parser.add_argument("--led_pin")
        self.arguments = vars(parser.parse_args())
        self.set_rabbitmq_properties()

    def set_rabbitmq_host_ip(self):
        self._rabbitmq_host_ip = self.arguments["rabbitmq_host_ip"]

    def set_security_config_exchange_name(self):
        self._security_config_queue_name = self.arguments["security_config_queue_name"]

    def set_security_config_queue_name(self):
        self._security_config_exchange_name = self.arguments["security_config_exchange_name"]

    def set_logging_property_file(self):
        self._logging_file_location = self.arguments["logging_file_location"]

    def set_pir_sensor_pin(self):
        if self.arguments['pir_sensor_pin'] is not None:
            self._pir_sensor_pin = self.arguments['pir_sensor_pin']
        else:
            self._pir_sensor_pin = 4

    def set_pir_num_readings(self):
        if self.arguments['pir_num_readings'] is not None:
            self._pir_num_readings = self.arguments['pir_num_readings']
        else:
            self._pir_num_readings = 10

    def set_pir_detections_per_second(self):
        if self.arguments['pir_detections_per_second'] is not None:
            self._pir_detections_per_second = self.arguments['pir_detections_per_second']
        else:
            self._pir_detections_per_second = 5

    def set_pir_threshold(self):
        if self.arguments['pir_threshold'] is not None:
            self._pir_threshold = self.arguments['pir_threshold']
        else:
            self._pir_threshold = 0.2

    def set_led_pin(self):
        if self.arguments["led_pin"] is not None:
            self._led_pin = self.arguments["led_pin"]
        else:
            self._led_pin = 17

    def set_security_micro_service_host_ip(self):
        self._security_micro_service_host_ip = self.arguments["security_micro_service_host_ip"]

    def set_security_micro_service_host_port(self):
        self._security_micro_service_host_port = self.arguments["security_micro_service_host_port"]
