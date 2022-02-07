class Subject:
    def __init__(self):
        self.observers = []
        self.state = None

    def set_state(self, state):
        self.state = state
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def add_observer(self, observer):
        self.observers.append(observer)

    def get_state(self):
        return self.state
