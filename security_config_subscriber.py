import json
import logging
import time

import pika
from pika.exceptions import AMQPConnectionError

from properties.security_camera_properties import SecurityCameraProperties
from security_config_receiver import SecurityConfigReceiver

LOGGER = logging.getLogger(__name__)


class SecurityConfigSubscriber(SecurityConfigReceiver):
    def __init__(self,
                 security_camera_properties: SecurityCameraProperties):
        self.rabbitmq_properties = security_camera_properties
        self.received_security_config = None

    def receive_security_config(self):
        while True:
            try:
                rabbitmq_host_ip = self.rabbitmq_properties.get_rabbitmq_host_ip()
                security_config_exchange_name = self.rabbitmq_properties.get_security_config_exchange_name()
                security_config_queue_name = self.rabbitmq_properties.get_security_config_queue_name()

                connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host=rabbitmq_host_ip)
                )
                channel = connection.channel()
                channel.exchange_declare(exchange=security_config_exchange_name,
                                         exchange_type='fanout',
                                         durable=True)
                channel.queue_declare(queue=security_config_queue_name)
                channel.queue_bind(exchange=security_config_exchange_name,
                                   queue=security_config_queue_name)
                channel.basic_consume(queue=security_config_queue_name,
                                      on_message_callback=self.process_message,
                                      auto_ack=True)
                LOGGER.info("Listening for messages...")
                channel.start_consuming()
            except AMQPConnectionError as e:
                LOGGER.error("An AMQPConnectionError has occurred: %r, this exception is eligible for reconnect.", e)
                time.sleep(5)
                LOGGER.info("Attempting to reconnect.")
                continue
            except Exception as e:
                LOGGER.error(
                    "Exception occurred listening to messages: %r, this exception is not eligible for reconnect.", e)
                raise

    def process_message(self, ch, method, properties, body):
        security_config_string = body.decode()
        security_config = json.loads(security_config_string)
        self.received_security_config = security_config
        LOGGER.info("New security config received: %s", security_config)
