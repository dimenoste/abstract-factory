from abc import ABC, abstractmethod

class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        return ''

class TransformCapability(ABC):

    @abstractmethod
    def transform(self) -> str:
        return ''

    @abstractmethod
    def revert(self) -> str:
        return ''
