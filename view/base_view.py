from controller.enumerators import ComandoUsuario
from screens.terminal.enumerators import Telas
from view.abstract_view import View


class BaseView(View):
    def __init__(self) -> None:
        super().__init__()

    def iniciar(self) -> None:
        self.screen_manager.trocar_de_tela(Telas.WELCOME)

    def inicio_deslogado(self) -> ComandoUsuario:
        self.screen_manager.trocar_de_tela(Telas.INICIO_DESLOGADO)
        comando_usuario = self.screen_manager.esperar_comando_usuario()

        match comando_usuario:
            case "1":
                return ComandoUsuario.LISTAR_IMOVEIS
            case "2":
                return self.__tela_de_cadastro_login()
            case "3":
                return ComandoUsuario.SAIR

    def sair_sistema(self) -> None:
        self.screen_manager.trocar_de_tela(Telas.AGRADECIMENTO)

    def __tela_de_cadastro_login(self) -> None:
        self.screen_manager.trocar_de_tela(Telas.CADASTRO_LOGIN)
        comando_usuario = self.screen_manager.esperar_comando_usuario()

        match comando_usuario:
            case "1":
                return ComandoUsuario.CADASTRAR_USUARIO
            case "2":
                return ComandoUsuario.LOGAR_USUARIO
            case "3":
                self.screen_manager.voltar_para_tela_anterior()
                self.processo()

    def logar_usuario(self) -> None:
        self.screen_manager.trocar_de_tela(Telas.LOGIN)
        comando_usuario = self.screen_manager.esperar_comando_usuario()
        return comando_usuario

    def cadastrar_usuario(self) -> None:
        self.screen_manager.trocar_de_tela(Telas.CADASTRO_USUARIO)
        comando_usuario = self.screen_manager.esperar_comando_usuario()

        match comando_usuario:
            case "1":
                return ComandoUsuario.CADASTRAR_LOCATARIO
            case "2":
                return ComandoUsuario.CADASTRAR_PROPRIETARIO
