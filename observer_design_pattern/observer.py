from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self, subject):
        self.subject = subject

    @abstractmethod
    def update(self):
        pass
