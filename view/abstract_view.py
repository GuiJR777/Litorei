from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def cadastrar(self, payload: dict) -> None:
        pass
