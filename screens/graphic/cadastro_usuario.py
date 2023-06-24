# https://flet.dev/docs/
from flet import (
    AppBar,
    ButtonStyle,
    colors,
    Column,
    icons,
    IconButton,
    Image,
    ImageFit,
    ImageRepeat,
    MainAxisAlignment,
    OutlinedButton,
    RoundedRectangleBorder,
    Row,
)

from screens.graphic.abstract_pages import Page
from utils.constants import ABSOLUTE_IMAGES_PATH

LOGO_LETTERS_IMAGE_PATH = (
    ABSOLUTE_IMAGES_PATH + "/logo-removedbg-only-letters.png"
)
LOCATARIO_IMAGE = ABSOLUTE_IMAGES_PATH + "/locatario.png"
PROPRIETARIO_IMAGE = ABSOLUTE_IMAGES_PATH + "/proprietario.png"


class CadastroUsuario(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
        self.controls = [
            # Menu da parte superior
            AppBar(
                leading=IconButton(
                    icons.ARROW_BACK_IOS, on_click=self.__voltar
                ),
                title=Image(
                    src=LOGO_LETTERS_IMAGE_PATH,
                    height=30,
                    fit=ImageFit.CONTAIN,
                    repeat=ImageRepeat.NO_REPEAT,
                ),
                bgcolor=colors.TEAL_ACCENT_700,
            ),  # Fim do menu da parte superior
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    OutlinedButton(
                                        text="Estou procurando um imóvel",
                                        width=480,
                                        height=480,
                                        content=Image(
                                            src=LOCATARIO_IMAGE,
                                            fit=ImageFit.CONTAIN,
                                            repeat=ImageRepeat.NO_REPEAT,
                                        ),
                                        on_click=self.__cadastrar_locatario,
                                        style=ButtonStyle(
                                            shape=RoundedRectangleBorder(
                                                radius=8
                                            )  # noqa
                                        ),
                                    ),  # EndButton
                                    OutlinedButton(
                                        text="Quero anunciar meus imóveis",
                                        width=480,
                                        height=480,
                                        content=Image(
                                            src=PROPRIETARIO_IMAGE,
                                            fit=ImageFit.CONTAIN,
                                            repeat=ImageRepeat.NO_REPEAT,
                                        ),
                                        on_click=self.__cadastrar_proprietario,
                                        style=ButtonStyle(
                                            shape=RoundedRectangleBorder(
                                                radius=8
                                            )  # noqa
                                        ),
                                    ),  # EndButton
                                ],
                                alignment=MainAxisAlignment.CENTER,
                            )  # EndRow
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

    def __cadastrar_locatario(self, event) -> None:
        self.preencher_payload(event, {"comando": "1"})

    def __cadastrar_proprietario(self, event) -> None:
        self.preencher_payload(event, {"comando": "2"})

    def __voltar(self, event) -> None:
        self.preencher_payload(event, {"comando": "3"})
