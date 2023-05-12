from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def __init__(self, screen_manager) -> None:
        pass
