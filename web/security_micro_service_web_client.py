import logging

import requests

from properties.security_camera_properties import SecurityCameraProperties

LOGGER = logging.getLogger(__name__)


class SecurityMicroServiceWebClient:
    def __init__(self,
                 security_camera_properties: SecurityCameraProperties):
        self._base_url = f"http://" \
                         f"{security_camera_properties.get_security_micro_service_host_ip()}:" \
                         f"{security_camera_properties.get_security_micro_service_host_port()}/" \
                         f"{security_camera_properties.get_security_micro_service_context_path()}"

    def send_image_for_security_check(self, encoded_image):
        security_check_url = f"{self._base_url}/security-check"

        response = requests.post(url=security_check_url,
                                 data=encoded_image)
        if not response.ok:
            LOGGER.error("Security micro-service returned a response other than 2xx: \n The status was:"
                         " %s \n The content was: %s \n", response.status_code, response.text)
        else:
            LOGGER.info("Security micro-service successfully processed the captured image.")
