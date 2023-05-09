from typing import Dict

from screens.terminal.abstract_screen import Screen
from screens.terminal.agradecimento import Agradecimento
from screens.terminal.cadastro_locatario import CadastroLocatario
from screens.terminal.cadastro_login import CadastroLogin
from screens.terminal.cadastro_usuario import CadastroUsuario
from screens.terminal.enumerators import Telas
from screens.terminal.inicio_deslogado import InicioDeslogado
from screens.terminal.login import Login
from screens.terminal.welcome import Welcome


class ScreenManager:
    def __init__(self) -> None:
        self.__telas: Dict[Telas, Screen] = {
            Telas.WELCOME: Welcome(),
            Telas.INICIO_DESLOGADO: InicioDeslogado(),
            Telas.AGRADECIMENTO: Agradecimento(),
            Telas.CADASTRO_LOGIN: CadastroLogin(),
            Telas.LOGIN: Login(),
            Telas.CADASTRO_USUARIO: CadastroUsuario(),
            Telas.CADASTRO_LOCATARIO: CadastroLocatario(),
        }
        self.__active_screen = None
        self.__last_screens = []

    def trocar_de_tela(self, tela: Telas) -> None:
        self.__last_screens.append(self.__active_screen)
        self.__active_screen = self.__telas[tela]
        self.__active_screen.entrada()

    def voltar_para_tela_anterior(self) -> None:
        self.__active_screen = self.__last_screens.pop()
        self.__active_screen.entrada()

    def esperar_comando_usuario(self) -> str:
        return self.__active_screen.campos()
