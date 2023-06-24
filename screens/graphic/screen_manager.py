from typing import Dict

from flet import Page as FletPage

from screens.abstract_screen_manager import ScreenManager
from screens.enumerators import Telas
from screens.graphic.abstract_pages import Page
from screens.graphic.cadastro_locatario import CadastroLocatario
from screens.graphic.cadastro_usuario import CadastroUsuario
from screens.graphic.inicio_deslogado import InicioDeslogado
from screens.graphic.welcome import Welcome
from screens.graphic.cadastro_login import CadastroLogin


TELAS_PARA_NAO_IMPLEMENTAR = [Telas.LOGIN]


class GUIScreenManager(ScreenManager):
    def __init__(self, page) -> None:
        self.__page: FletPage = page
        self.__telas: Dict[Telas, Page] = {
            # Telas.AGRADECIMENTO: Agradecimento,
            # Telas.CADASTRO_IMOVEL: CadastroImovel,
            Telas.CADASTRO_LOCATARIO: CadastroLocatario,
            Telas.CADASTRO_LOGIN: CadastroLogin,
            # Telas.CADASTRO_PROPRIETARIO: CadastroProprietario,
            Telas.CADASTRO_USUARIO: CadastroUsuario,
            # Telas.DIARIAS: Diarias,
            # Telas.EDITAR_IMOVEL: EditarImovel,
            # Telas.EDITAR_PERFIL_LOCATARIO: EditarPerfilLocatario,
            # Telas.EDITAR_PERFIL_PROPRIETARIO: EditarPerfilProprietario,
            Telas.INICIO_DESLOGADO: InicioDeslogado,
            # Telas.INICIO_LOCATARIO: InicioLocatario,
            # Telas.INICIO_PROPRIETARIO: InicioProprietario,
            # Telas.LISTAGEM_IMOVEIS: ListagemImoveis,
            # Telas.MOSTRAR_IMOVEL: MostrarImovel,
            # Telas.MOSTRAR_IMOVEIS_PROPRIETARIO: MostrarImoveisProprietario,
            # Telas.PERFIL_LOCATARIO: PerfilLocatario,
            # Telas.PERFIL_PROPRIETARIO: PerfilProprietario,
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
        self.__active_page = self.__telas[tela](tela.value)
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
        banner = self.__active_page.start_success_banner("Concluido", mensagem)
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
