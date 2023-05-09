from abc import ABC, abstractmethod

from screens.terminal.screens_manager import ScreenManager


class View(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.__screen_manager = ScreenManager()

    @abstractmethod
    def iniciar(self) -> None:
        pass

    @property
    def screen_manager(self) -> ScreenManager:
        return self.__screen_manager
