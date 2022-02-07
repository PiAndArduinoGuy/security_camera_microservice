import argparse

from properties.rabbitmq_properties import RabbitMqProperties


class RabbitMqCommandLineProperties(RabbitMqProperties):
    def __init__(self):
        super().__init__()
        parser = argparse.ArgumentParser()
        parser.add_argument("--rabbitmq_host_ip", required=True)
        parser.add_argument("--security_config_queue_name", required=True)
        parser.add_argument("--security_config_exchange_name", required=True)
        self.arguments = vars(parser.parse_args())
        self.set_rabbitmq_properties()

    def set_rabbitmq_host_ip(self):
        self._rabbitmq_host_ip = self.arguments["rabbitmq_host_ip"]

    def set_security_config_exchange_name(self):
        self._security_config_queue_name = self.arguments["security_config_queue_name"]

    def set_security_config_queue_name(self):
        self._security_config_exchange_name = self.arguments["security_config_exchange_name"]
