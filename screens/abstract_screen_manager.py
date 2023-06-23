from abc import ABC, abstractmethod

from screens.enumerators import Telas


class ScreenManager(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def trocar_de_tela(self, tela: Telas, **kwargs) -> None:
        pass

    @abstractmethod
    def esperar_comando_usuario(self) -> str:
        pass

    @abstractmethod
    def feedback_sucesso(self, mensagem: str) -> None:
        pass

    @abstractmethod
    def feedback_erro(self, mensagem: str) -> None:
        pass
