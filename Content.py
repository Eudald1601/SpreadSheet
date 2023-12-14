from abc import ABC, abstractmethod

class Content(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def getNumericalValue(self, content):
        pass

    @abstractmethod
    def getTextualValue(self, content):
        pass