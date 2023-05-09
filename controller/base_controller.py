from controller.abstract_controller import Controller
from controller.enumerators import ComandoUsuario
from controller.imovel import ImovelController
from controller.locatario import LocatarioController
from controller.proprietario import ProprietarioController
from view.base_view import BaseView


class BaseController(Controller):
    def __init__(self) -> None:
        self.__usuario_logado = None
        self.__imovel = ImovelController(self)
        self.__locatario = LocatarioController(self)
        self.__proprietario = ProprietarioController(self)
        self.__view = BaseView()

    def iniciar(self) -> None:
        self.__view.iniciar()
        self.processo()

    def processo(self) -> None:
        comando_usuario = self.__view.inicio_deslogado()
        match comando_usuario:
            case ComandoUsuario.SAIR:
                self.sair()
            case ComandoUsuario.LOGAR_USUARIO:
                self.logar()
            case ComandoUsuario.CADASTRAR_USUARIO:
                self.cadastrar_usuario()

    def sair(self) -> None:
        self.__view.sair_sistema()

    def logar(self) -> None:
        resposta = self.__view.logar_usuario()

        if (
            resposta["email"] == "john.due@email.com"
            and resposta["senha"] == "123456"
        ):
            self.__usuario_logado = resposta
            print("Logado com sucesso!")  # TODO: Remover

    def cadastrar_usuario(self) -> None:
        resposta = self.__view.cadastrar_usuario()

        match resposta:
            case ComandoUsuario.CADASTRAR_LOCATARIO:
                self.__locatario.cadastrar()
