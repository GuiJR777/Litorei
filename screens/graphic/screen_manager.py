from typing import Dict

from flet import Page as FletPage

from screens.abstract_screen_manager import ScreenManager
from screens.enumerators import Telas
from screens.graphic.abstract_pages import Page
from screens.graphic.cadastro_imovel import CadastroImovel
from screens.graphic.cadastro_locatario import CadastroLocatario
from screens.graphic.cadastro_proprietario import CadastroProprietario
from screens.graphic.cadastro_usuario import CadastroUsuario
from screens.graphic.diarias import Diarias
from screens.graphic.editar_imovel import EditarImovel
from screens.graphic.editar_perfil_locatario import EditarPerfilLocatario
from screens.graphic.editar_perfil_proprietario import EditarPerfilProprietario
from screens.graphic.inicio_deslogado import InicioDeslogado
from screens.graphic.inicio_locatario import InicioLocatario
from screens.graphic.inicio_proprietario import InicioProprietario
from screens.graphic.listagem_imoveis import ListagemImoveis
from screens.graphic.mostrar_imoveis_proprietario import (
    MostrarImoveisProprietario,
)
from screens.graphic.mostrar_imovel import MostrarImovel
from screens.graphic.perfil_locatario import PerfilLocatario
from screens.graphic.perfil_proprietario import PerfilProprietario
from screens.graphic.tipo_usuario import TipoUsuario
from screens.graphic.welcome import Welcome
from screens.graphic.cadastro_login import CadastroLogin


TELAS_PARA_NAO_IMPLEMENTAR = [Telas.LOGIN]


class GUIScreenManager(ScreenManager):
    def __init__(self, page) -> None:
        self.__page: FletPage = page
        self.__telas: Dict[Telas, Page] = {
            Telas.CADASTRO_IMOVEL: CadastroImovel,
            Telas.CADASTRO_LOCATARIO: CadastroLocatario,
            Telas.CADASTRO_LOGIN: CadastroLogin,
            Telas.CADASTRO_PROPRIETARIO: CadastroProprietario,
            Telas.CADASTRO_USUARIO: CadastroUsuario,
            Telas.DIARIAS: Diarias,
            Telas.EDITAR_IMOVEL: EditarImovel,
            Telas.EDITAR_PERFIL_LOCATARIO: EditarPerfilLocatario,
            Telas.EDITAR_PERFIL_PROPRIETARIO: EditarPerfilProprietario,
            Telas.INICIO_DESLOGADO: InicioDeslogado,
            Telas.INICIO_LOCATARIO: InicioLocatario,
            Telas.INICIO_PROPRIETARIO: InicioProprietario,
            Telas.LISTAGEM_IMOVEIS: ListagemImoveis,
            Telas.MOSTRAR_IMOVEL: MostrarImovel,
            Telas.MOSTRAR_IMOVEIS_PROPRIETARIO: MostrarImoveisProprietario,
            Telas.PERFIL_LOCATARIO: PerfilLocatario,
            Telas.PERFIL_PROPRIETARIO: PerfilProprietario,
            # Telas.RELATORIO_ALUGUEIS: RelatorioAlugueis,
            # Telas.VER_CONTRATO_ALUGUEL: ContratoAluguel,
            Telas.WELCOME: Welcome,
        }
        self.__active_page = None

    def trocar_de_tela(self, tela: Telas, **kwargs) -> None:
        if tela in TELAS_PARA_NAO_IMPLEMENTAR:
            del self.__active_page.payload["comando"]
            return

        if self.__active_page:
            if tela.value == self.__active_page.route:
                self.__active_page.payload = {}
                return

        self.__page.views.clear()
        usuario_logado = (
            self.__active_page.usuario_logado
            if self.__active_page
            else TipoUsuario.DESLOGADO
        )  # noqa
        self.__active_page = self.__telas[tela](tela.value)
        self.__active_page.usuario_logado = usuario_logado
        if kwargs != {}:
            self.__active_page.data = kwargs.get("data")
        self.__page.views.append(self.__active_page)
        self.__page.go(tela.value)

    def esperar_comando_usuario(self) -> str:
        self.__active_page.exibir_pagina()
        self.__page.update()

        while not self.__active_page.payload:
            self.__page.update()
        else:
            if "comando" in self.__active_page.payload:
                return self.__active_page.payload["comando"]
            return self.__active_page.payload

    def feedback_sucesso(self, mensagem: str) -> None:
        banner = self.__active_page.start_success_banner(mensagem)
        self.__page.banner = banner
        banner.open = True
        self.__page.banner.actions[0].on_click = self.__close_banner

    def feedback_erro(self, mensagem: str) -> None:
        banner = self.__active_page.start_alert_banner(mensagem)
        self.__page.banner = banner
        banner.open = True
        self.__page.banner.actions[0].on_click = self.__close_banner

    def __close_banner(self, event) -> None:
        self.__page.banner.open = False
        self.__page.update()
