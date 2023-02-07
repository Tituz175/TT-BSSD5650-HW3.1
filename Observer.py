from abc import ABC, abstractmethod


class AbstractSubject(ABC):
    @abstractmethod
    def register(self, listener):
        pass

    @abstractmethod
    def unregister(self, listener):
        pass

    @abstractmethod
    def notify_listeners(self, events):
        pass


class IListener(ABC):
    @abstractmethod
    def notify(self, event):
        pass


class Listener(IListener):
    def __init__(self, name, subject):
        self.name = name
        subject.register(self)

    def notify(self, event):
        print(self.name, "received event", event)


class Subject(AbstractSubject):
    def __init__(self):
        self.listeners = []
        self.data = None

    def getUserAction(self):
        self.data = input('Enter something to do:')
        return self.data

    # Implement abstract Class AbstractSubject

    def register(self, listener):
        self.listeners.append(listener)

    def unregister(self, listener):
        self.listeners.remove(listener)

    def notify_listeners(self, event):
        for listener in self.listeners:
            listener.notify(event)
