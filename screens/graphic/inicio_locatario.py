from flet import (
    AppBar,
    ButtonStyle,
    Column,
    Container,
    Image,
    ImageFit,
    ImageRepeat,
    MainAxisAlignment,
    Margin,
    OutlinedButton,
    Padding,
    PopupMenuButton,
    PopupMenuItem,
    RoundedRectangleBorder,
    Row,
    Text,
    TextButton,
    TextThemeStyle,
    icons,
)

from screens.graphic.abstract_pages import Page
from screens.graphic.tipo_usuario import TipoUsuario
from utils.constants import ABSOLUTE_IMAGES_PATH

LOGO_LETTERS_IMAGE_PATH = (
    ABSOLUTE_IMAGES_PATH + "/logo-removedbg-only-letters.png"
)
LISTA_IMOVEIS_IMAGE = ABSOLUTE_IMAGES_PATH + "/lista_imoveis.png"
CONTRATOS_IMAGE = ABSOLUTE_IMAGES_PATH + "/contratos.png"


class InicioLocatario(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
        self.usuario_logado = TipoUsuario.LOCATARIO
        self.padding = Padding(16, 48, 16, 48)

        self.controls = [
            # Menu da parte superior
            AppBar(
                title=Image(
                    src=LOGO_LETTERS_IMAGE_PATH,
                    height=30,
                    fit=ImageFit.CONTAIN,
                    repeat=ImageRepeat.NO_REPEAT,
                ),
                #
                actions=[
                    Container(
                        content=Row(
                            [
                                PopupMenuButton(
                                    icon=icons.PERSON_2_OUTLINED,
                                    items=[
                                        PopupMenuItem(
                                            content=TextButton(
                                                "Perfil",
                                                on_click=self.__acessar_perfil,  # noqa
                                            )
                                        ),
                                        PopupMenuItem(
                                            content=TextButton(
                                                "Contratos",
                                                on_click=self.__acessar_contratos,  # noqa
                                            )
                                        ),
                                        PopupMenuItem(
                                            content=TextButton(
                                                "Deslogar",
                                                on_click=self.__deslogar,  # noqa
                                            )
                                        ),
                                    ],
                                ),  # End of PopupMenuButton
                            ],
                            spacing=48,
                            alignment=MainAxisAlignment.START,
                        ),
                        margin=Margin(48, 0, 48, 0),
                    ),
                ],
            ),
            # Fim do menu da parte superior
            # Corpo da página
            Row(
                [
                    Column(
                        [
                            Text(
                                f"Bem vindo(a), {self.data['name']}",
                                style=TextThemeStyle.TITLE_LARGE,
                            ),
                            Row(
                                [
                                    OutlinedButton(
                                        text="Lista de imóveis",
                                        width=360,
                                        height=360,
                                        content=Image(
                                            src=LISTA_IMOVEIS_IMAGE,
                                            fit=ImageFit.CONTAIN,
                                            repeat=ImageRepeat.NO_REPEAT,
                                        ),
                                        on_click=self.__listagem_imoveis,
                                        style=ButtonStyle(
                                            shape=RoundedRectangleBorder(
                                                radius=8
                                            )  # noqa
                                        ),
                                    ),  # EndButton
                                    OutlinedButton(
                                        text="Quero anunciar meus imóveis",
                                        width=360,
                                        height=360,
                                        content=Image(
                                            src=CONTRATOS_IMAGE,
                                            fit=ImageFit.CONTAIN,
                                            repeat=ImageRepeat.NO_REPEAT,
                                        ),
                                        on_click=self.__acessar_contratos,
                                        style=ButtonStyle(
                                            shape=RoundedRectangleBorder(
                                                radius=8
                                            )  # noqa
                                        ),
                                    ),  # EndButton
                                ],
                                alignment=MainAxisAlignment.CENTER,
                            ),  # EndRow
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        height=800,
                    )  # EndColumn
                ],
                alignment=MainAxisAlignment.CENTER,
            ),  # EndRow
        ]

    def preencher_payload(self, event, content: dict) -> None:
        self.payload = content

    def __listagem_imoveis(self, event) -> None:
        self.preencher_payload(
            event,
            {"comando": "1"},
        )

    def __acessar_perfil(self, event) -> None:
        self.preencher_payload(
            event,
            {"comando": "2"},
        )

    def __acessar_contratos(self, event) -> None:
        self.preencher_payload(
            event,
            {"comando": "3"},
        )

    def __deslogar(self, event) -> None:
        self.preencher_payload(
            event,
            {"comando": "4"},
        )
