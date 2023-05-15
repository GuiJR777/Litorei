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
from screens.terminal.editar_perfil_proprietario import (
    EditarPerfilProprietario,
)
from screens.terminal.perfil_locatario import PerfilLocatario
from screens.terminal.editar_perfil_locatario import EditarPerfilLocatario
from screens.terminal.mostrar_imoveis_proprietario import (
    MostrarImoveisProprietario,
)
from screens.terminal.mostrar_imovel import MostrarImovel
from screens.terminal.contrato_aluguel import ContratoAluguel
from screens.terminal.editar_imovel import EditarImovel
from screens.terminal.diarias import Diarias
from screens.terminal.relatorio_alugueis import RelatorioAlugueis


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
            Telas.PERFIL_LOCATARIO: PerfilLocatario,
            Telas.EDITAR_PERFIL_LOCATARIO: EditarPerfilLocatario,
            Telas.MOSTRAR_IMOVEIS_PROPRIETARIO: MostrarImoveisProprietario,
            Telas.MOSTRAR_IMOVEL: MostrarImovel,
            Telas.VER_CONTRATO_ALUGUEL: ContratoAluguel,
            Telas.EDITAR_IMOVEL: EditarImovel,
            Telas.DIARIAS: Diarias,
            Telas.RELATORIO_ALUGUEIS: RelatorioAlugueis,
        }
        self.__active_screen = None

    def trocar_de_tela(self, tela: Telas, **kwargs) -> None:
        self.__active_screen = self.__telas[tela]()
        self.__active_screen.entrada(**kwargs)

    def esperar_comando_usuario(self) -> str:
        return self.__active_screen.campos()

    def feedback_sucesso(self, mensagem: str) -> None:
        self.__active_screen.show_success(mensagem)

    def feedback_erro(self, mensagem: str) -> None:
        self.__active_screen.show_error(mensagem)
