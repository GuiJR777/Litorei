from abc import ABC, abstractmethod


class Controller(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass
