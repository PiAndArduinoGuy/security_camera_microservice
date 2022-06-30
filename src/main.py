from logging_setup import LoggingSetup
from observer.movement_sensor import MovementSensor
from properties.security_camera_command_line_properties import SecurityCameraCommandLineProperties
from properties.security_camera_properties import SecurityCameraProperties
from subject.security_config_receiver import SecurityConfigReceiver
from subject.security_config_subscriber import SecurityConfigSubscriber
from web.security_micro_service_web_client import SecurityMicroServiceWebClient

if __name__ == '__main__':
    security_camera_properties: SecurityCameraProperties = SecurityCameraCommandLineProperties()
    logging_setup = LoggingSetup(security_camera_properties.get_logging_file_location())
    security_config_receiver: SecurityConfigReceiver = SecurityConfigSubscriber(security_camera_properties)
    security_micro_service_web_client = SecurityMicroServiceWebClient(security_camera_properties)
    movement_sensor = MovementSensor(security_config_receiver,
                                     security_camera_properties,
                                     security_micro_service_web_client)
    security_config_receiver.receive_security_config()
