from abc import ABC, abstractmethod

from properties.validation.properties_validator import PropertiesValidator


class RabbitMqProperties(ABC):
    def __init__(self):
        self._rabbitmq_host_ip = None
        self._security_config_exchange_name = None
        self._security_config_queue_name = None
        self._logging_file_location = None

    def get_rabbitmq_host_ip(self):
        PropertiesValidator.validate_property_non_none(self._rabbitmq_host_ip)
        return self._rabbitmq_host_ip

    def get_security_config_exchange_name(self):
        PropertiesValidator.validate_property_non_none(self._security_config_exchange_name)
        return self._security_config_exchange_name

    def get_security_config_queue_name(self):
        PropertiesValidator.validate_property_non_none(self._security_config_queue_name)
        return self._security_config_queue_name

    @abstractmethod
    def set_rabbitmq_host_ip(self):
        pass

    @abstractmethod
    def set_security_config_exchange_name(self):
        pass

    @abstractmethod
    def set_security_config_queue_name(self):
        pass

    def get_logging_file_location(self):
        PropertiesValidator.validate_property_non_none(self._logging_file_location)
        return self._logging_file_location

    @abstractmethod
    def set_logging_property_file(self):
        pass

    def set_rabbitmq_properties(self):
        self.set_rabbitmq_host_ip()
        self.set_security_config_queue_name()
        self.set_security_config_exchange_name()
        self.set_logging_property_file()
