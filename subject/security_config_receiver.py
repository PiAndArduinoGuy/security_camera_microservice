from abc import ABC, abstractmethod

from observer_design_pattern.subject import Subject


class SecurityConfigReceiver(ABC, Subject):

    @abstractmethod
    def receive_security_config(self):
        pass


