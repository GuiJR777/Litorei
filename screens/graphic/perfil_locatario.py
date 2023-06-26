# https://flet.dev/docs/
from flet import (
    AppBar,
    Column,
    ElevatedButton,
    IconButton,
    Image,
    ImageFit,
    ImageRepeat,
    MainAxisAlignment,
    Row,
    Text,
    TextThemeStyle,
    icons,
)

from screens.graphic.abstract_pages import Page
from utils.constants import ABSOLUTE_IMAGES_PATH

LOGO_LETTERS_IMAGE_PATH = (
    ABSOLUTE_IMAGES_PATH + "/logo-removedbg-only-letters.png"
)


class PerfilLocatario(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
        self.nome = Text(f"Nome: {self.data.get('nome')}")
        self.email = Text(f"Email: {self.data.get('email')}")
        self.documento = Text(f"CPF: {self.data.get('documento')}")
        self.telefone = Text(f"Telefone: {self.data.get('telefone')}")

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
            ),
            # Fim do menu da parte superior
            Row(
                [
                    Column(
                        [
                            Text(
                                "Seu perfil",
                                style=TextThemeStyle.TITLE_LARGE,
                            ),
                            self.nome,
                            self.documento,
                            self.telefone,
                            self.email,
                            ElevatedButton(
                                "Editar",
                                icon="edit",
                                on_click=self.__edit_register,  # noqa
                            ),  # EndButton
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        width=480,
                        height=800,
                    )  # EndColumn
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        ]

    def preencher_payload(self, event, content: dict) -> None:
        self.payload = content

    def __edit_register(self, event) -> None:
        self.preencher_payload(event, {"comando": "1"})

    def __voltar(self, event) -> None:
        self.preencher_payload(event, {"comando": "2"})
