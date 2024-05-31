import abc

class Adapter(abc.ABC):
    @abc.abstractmethod
    def connect(self, on_connect):
        pass

    @abc.abstractmethod
    def search(self):
        pass
