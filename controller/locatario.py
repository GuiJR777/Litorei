from controller.abstract_controller import Controller
from controller.enumerators import ComandoUsuario
from view.locatario import LocatarioView
from model.locatario import Locatario


class LocatarioController(Controller):
    def __init__(self, base_controller) -> None:
        self.__locatarios = []
        self.__base_controller = base_controller
        self.__locatario_view = LocatarioView(
            self.__base_controller.screen_manager)

    def cadastrar(self) -> None:
        dados_locatario = self.__locatario_view.cadastrar()

        if isinstance(dados_locatario, ComandoUsuario):
            if dados_locatario == ComandoUsuario.VOLTAR:
                self.__base_controller.cadastrar_usuario()

        novo_locatario = Locatario(**dados_locatario)
        self.__locatarios.append(novo_locatario)
        self.__locatario_view.cadastrado_com_sucesso()
        self.__base_controller.usuario_logado = novo_locatario
        self.__base_controller.inicio_deslogado()  # TODO: Trocar para inicio locatario
