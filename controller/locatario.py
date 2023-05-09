from controller.abstract_controller import Controller
from view.locatario import LocatarioView
from model.locatario import Locatario


class LocatarioController(Controller):
    def __init__(self, base_controller) -> None:
        self.__locatarios = []
        self.__base_controller = base_controller
        self.__locatario_view = LocatarioView()

    def iniciar(self) -> None:
        pass

    def processo(self) -> None:
        pass

    def cadastrar(self) -> None:
        dados_locatario = self.__locatario_view.cadastrar()
        novo_locatario = Locatario(**dados_locatario)
        self.__locatarios.append(novo_locatario)