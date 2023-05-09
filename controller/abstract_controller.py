from abc import ABC, abstractmethod


class Controller(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def iniciar(self) -> None:
        pass

    @abstractmethod
    def processo(self) -> None:
        pass
