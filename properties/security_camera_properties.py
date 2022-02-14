from abc import ABC, abstractmethod

from properties.validation.properties_validator import PropertiesValidator


class SecurityCameraProperties(ABC):
    def __init__(self):
        self._rabbitmq_host_ip = None
        self._security_config_exchange_name = None
        self._security_config_queue_name = None
        self._logging_file_location = None
        self._pir_sensor_pin = None
        self._pir_num_readings = None
        self._pir_detections_per_second = None
        self._pir_threshold = None
        self._led_pin = None
        self._security_micro_service_host_ip = None
        self._security_micro_service_host_port = None
        self._security_micro_service_context_path = None
        self._security_camera_microservice_capture_directory = None

    def get_rabbitmq_host_ip(self):
        PropertiesValidator.validate_property_non_none(self._rabbitmq_host_ip)
        return self._rabbitmq_host_ip

    def get_security_config_exchange_name(self):
        PropertiesValidator.validate_property_non_none(self._security_config_exchange_name)
        return self._security_config_exchange_name

    def get_security_config_queue_name(self):
        PropertiesValidator.validate_property_non_none(self._security_config_queue_name)
        return self._security_config_queue_name

    def get_logging_file_location(self):
        PropertiesValidator.validate_property_non_none(self._logging_file_location)
        return self._logging_file_location

    def get_pir_sensor_pin(self):
        PropertiesValidator.validate_property_non_none(self._pir_sensor_pin)
        return self._pir_sensor_pin

    def get_pir_num_readings(self):
        PropertiesValidator.validate_property_non_none(self._pir_num_readings)
        return self._pir_num_readings

    def get_pir_detections_per_second(self):
        PropertiesValidator.validate_property_non_none(self._pir_detections_per_second)
        return self._pir_detections_per_second

    def get_pir_threshold(self):
        PropertiesValidator.validate_property_non_none(self._pir_threshold)
        return self._pir_threshold

    def get_led_pin(self):
        PropertiesValidator.validate_property_non_none(self._led_pin)
        return self._led_pin

    def get_security_micro_service_host_ip(self):
        PropertiesValidator.validate_property_non_none(self._security_micro_service_host_ip)
        return self._security_micro_service_host_ip

    def get_security_micro_service_host_port(self):
        PropertiesValidator.validate_property_non_none(self._security_micro_service_host_port)
        return self._security_micro_service_host_port

    def get_security_micro_service_context_path(self):
        PropertiesValidator.validate_property_non_none(self._security_micro_service_context_path)
        return self._security_micro_service_context_path

    def get_security_camera_microservice_capture_directory(self):
        PropertiesValidator.validate_property_non_none(self._security_camera_microservice_capture_directory)

    @abstractmethod
    def set_rabbitmq_host_ip(self):
        pass

    @abstractmethod
    def set_security_config_exchange_name(self):
        pass

    @abstractmethod
    def set_security_config_queue_name(self):
        pass

    @abstractmethod
    def set_logging_property_file(self):
        pass

    @abstractmethod
    def set_pir_sensor_pin(self):
        pass

    @abstractmethod
    def set_pir_num_readings(self):
        pass

    @abstractmethod
    def set_pir_detections_per_second(self):
        pass

    @abstractmethod
    def set_pir_threshold(self):
        pass

    @abstractmethod
    def set_led_pin(self):
        pass

    @abstractmethod
    def set_security_micro_service_host_ip(self):
        pass

    @abstractmethod
    def set_security_micro_service_host_port(self):
        pass

    @abstractmethod
    def set_security_micro_service_context_path(self):
        pass

    @abstractmethod
    def set_security_camera_microservice_capture_directory(self):
        pass

    def set_rabbitmq_properties(self):
        self.set_rabbitmq_host_ip()
        self.set_security_config_queue_name()
        self.set_security_config_exchange_name()
        self.set_logging_property_file()
        self.set_pir_sensor_pin()
        self.set_pir_threshold()
        self.set_pir_detections_per_second()
        self.set_pir_num_readings()
        self.set_led_pin()
        self.set_security_micro_service_host_port()
        self.set_security_micro_service_host_ip()
        self.set_security_micro_service_context_path()
        self.set_security_camera_microservice_capture_directory()
