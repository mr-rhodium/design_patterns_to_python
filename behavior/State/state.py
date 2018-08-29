from abc import ABCMeta, abstractmethod

class State:
    metaclass = ABCMeta
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def puse(self):
        pass

    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def take(self):
        pass
