from controller.abstract_controller import Controller
from controller.enumerators import ComandoUsuario
from controller.imovel import ImovelController
from controller.locatario import LocatarioController
from controller.proprietario import ProprietarioController
from model.proprietario import Proprietario
from model.usuario import Usuario
from view.base_view import BaseView
from model.locatario import Locatario


class BaseController(Controller):
    def __init__(self, screen_manager) -> None:
        self.__screen_manager = screen_manager
        self.__usuario_logado = None
        self.__imovel = ImovelController(self)
        self.__locatario = LocatarioController(self)
        self.__proprietario = ProprietarioController(self)
        self.__view = BaseView(screen_manager)
        self.__first_iniciation = True

    @property
    def usuario_logado(self) -> dict:
        return self.__usuario_logado

    @usuario_logado.setter
    def usuario_logado(self, usuario: Usuario) -> None:
        self.__usuario_logado = usuario

    @property
    def screen_manager(self):
        return self.__screen_manager

    @property
    def imovel(self) -> ImovelController:
        return self.__imovel

    @property
    def locatario(self) -> LocatarioController:
        return self.__locatario

    def iniciar(self) -> None:
        if self.__first_iniciation:
            self.__view.iniciar()
            self.__first_iniciation = False

        if self.usuario_logado:
            if isinstance(self.usuario_logado, Locatario):
                self.__locatario.iniciar()
            elif isinstance(self.usuario_logado, Proprietario):
                self.__proprietario.iniciar()
        else:
            self.inicio_deslogado()

    def inicio_deslogado(self) -> None:
        comando_usuario = self.__view.inicio_deslogado()
        match comando_usuario:
            case ComandoUsuario.SAIR:
                self.sair()
            case ComandoUsuario.IR_CADASTRO_LOGIN:
                self.tela_de_cadastro_login()
            case ComandoUsuario.LISTAR_IMOVEIS:
                self.__imovel.listar_imoveis()

    def sair(self) -> None:
        self.__view.sair_sistema()

    def tela_de_cadastro_login(self) -> None:
        comando_usuario = self.__view.tela_de_cadastro_login()
        match comando_usuario:
            case ComandoUsuario.VOLTAR:
                self.inicio_deslogado()
            case ComandoUsuario.LOGAR_USUARIO:
                self.logar()
            case ComandoUsuario.CADASTRAR_USUARIO:
                self.cadastrar_usuario()

    def logar(self) -> None:
        resposta = self.__view.logar_usuario()

        if isinstance(resposta, ComandoUsuario):
            match resposta:
                case ComandoUsuario.VOLTAR:
                    self.tela_de_cadastro_login()

        for locatario in self.__locatario.locatarios:
            if locatario.email == resposta["email"]:
                if locatario.senha == resposta["senha"]:
                    self.__usuario_logado = locatario
                    self.__locatario.iniciar()
                else:
                    self.__view.erro_login("Senha incorreta!")
                    self.tela_de_cadastro_login()

        for proprietario in self.__proprietario.proprietarios:
            if proprietario.email == resposta["email"]:
                if proprietario.senha == resposta["senha"]:
                    self.__usuario_logado = proprietario
                    self.__proprietario.iniciar()
                else:
                    self.__view.erro_login("Senha incorreta!")
                    self.tela_de_cadastro_login()

        self.__view.erro_login("Usuário não encontrado!")

    def cadastrar_usuario(self) -> None:
        resposta = self.__view.cadastrar_usuario()

        match resposta:
            case ComandoUsuario.CADASTRAR_LOCATARIO:
                self.__locatario.cadastrar()
            case ComandoUsuario.CADASTRAR_PROPRIETARIO:
                self.__proprietario.cadastrar()
            case ComandoUsuario.VOLTAR:
                self.tela_de_cadastro_login()
