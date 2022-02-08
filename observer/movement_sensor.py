import base64
import logging

from observer_design_pattern.observer import Observer
from observer_design_pattern.subject import Subject

LOGGER = logging.getLogger(__name__)


class MovementSensor(Observer):
    def __init__(self,
                 subject: Subject):
        super().__init__(subject)
        self.subject.add_observer(self)

    def update(self):
        security_config = self.subject.get_state()
        security_state = security_config["securityState"]
        if security_state == 'ARMED':
            LOGGER.info("Security state is ARMED, motion detecting will be enabled.")
        elif security_state == 'DISARMED':
            LOGGER.info("Security state is DISARMED, motion detecting will be disabled.")
