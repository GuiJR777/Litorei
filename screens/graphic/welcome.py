from flet import (
    Column,
    ElevatedButton,
    Image,
    ImageFit,
    ImageRepeat,
    MainAxisAlignment,
    Row,
    Text,
    TextThemeStyle,
    colors,
)

from screens.graphic.abstract_pages import Page
from utils.constants import ABSOLUTE_IMAGES_PATH

LOGO_IMAGE_PATH = ABSOLUTE_IMAGES_PATH + "/logo-removedbg.png"


class Welcome(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
        self.controls = [
            Column(
                [
                    Row(
                        [
                            Text(
                                "Bem vindo ao...",
                                style=TextThemeStyle.HEADLINE_LARGE,
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),  # EndRow

                    Row(
                        [
                            Image(
                                src=LOGO_IMAGE_PATH,
                                height=240,
                                fit=ImageFit.CONTAIN,
                                repeat=ImageRepeat.NO_REPEAT,
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),  # EndRow

                    Row(
                        [
                            ElevatedButton(
                                "Entrar", on_click=self.preencher_payload
                            ),  # EndButton
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),  # EndRow
                ],
                alignment=MainAxisAlignment.SPACE_AROUND,
                height=1000,
            ),  # EndColumn
        ]

    def preencher_payload(self, event) -> None:
        self.payload = {"comando": "entrar"}
