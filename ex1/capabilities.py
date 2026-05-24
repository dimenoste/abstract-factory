from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        return ""


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        self.transformed = True
        return ""

    @abstractmethod
    def revert(self) -> str:
        self.transformed = False
        return ""
