from abc import ABC, abstractmethod


class SecurityConfigReceiver(ABC):

    @abstractmethod
    def receive_security_config(self):
        pass
