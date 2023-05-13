from typing import Dict

from screens.terminal.abstract_screen import Screen
from screens.terminal.agradecimento import Agradecimento
from screens.terminal.cadastro_locatario import CadastroLocatario
from screens.terminal.cadastro_login import CadastroLogin
from screens.terminal.cadastro_usuario import CadastroUsuario
from screens.terminal.enumerators import Telas
from screens.terminal.inicio_deslogado import InicioDeslogado
from screens.terminal.inicio_locatario import InicioLocatario
from screens.terminal.listagem_imoveis import ListagemImoveis
from screens.terminal.login import Login
from screens.terminal.perfil_proprietario import PerfilProprietario
from screens.terminal.welcome import Welcome
from screens.terminal.cadastro_proprietario import CadastroProprietario
from screens.terminal.cadastro_imovel import CadastroImovel
from screens.terminal.inicio_proprietario import InicioProprietario
from screens.terminal.editar_perfil_proprietario import EditarPerfilProprietario


class ScreenManager:
    def __init__(self) -> None:
        self.__telas: Dict[Telas, Screen] = {
            Telas.AGRADECIMENTO: Agradecimento,
            Telas.CADASTRO_LOCATARIO: CadastroLocatario,
            Telas.CADASTRO_LOGIN: CadastroLogin,
            Telas.CADASTRO_USUARIO: CadastroUsuario,
            Telas.INICIO_DESLOGADO: InicioDeslogado,
            Telas.INICIO_LOCATARIO: InicioLocatario,
            Telas.LISTAGEM_IMOVEIS: ListagemImoveis,
            Telas.LOGIN: Login,
            Telas.WELCOME: Welcome,
            Telas.CADASTRO_PROPRIETARIO: CadastroProprietario,
            Telas.CADASTRO_IMOVEL: CadastroImovel,
            Telas.INICIO_PROPRIETARIO: InicioProprietario,
            Telas.PERFIL_PROPRIETARIO: PerfilProprietario,
            Telas.EDITAR_PERFIL_PROPRIETARIO: EditarPerfilProprietario,
        }
        self.__active_screen = None
        self.__last_screens = []

    def trocar_de_tela(self, tela: Telas, **kwargs) -> None:
        self.__last_screens.append(self.__active_screen)
        self.__active_screen = self.__telas[tela]()
        self.__active_screen.entrada(**kwargs)

    def voltar_para_tela_anterior(self) -> None:
        self.__active_screen = self.__last_screens.pop()
        self.__active_screen.entrada()

    def esperar_comando_usuario(self) -> str:
        return self.__active_screen.campos()

    def feedback_sucesso(self, mensagem: str) -> None:
        self.__active_screen.show_success(mensagem)

    def feedback_erro(self, mensagem: str) -> None:
        self.__active_screen.show_error(mensagem)
