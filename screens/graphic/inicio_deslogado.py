from flet import (AppBar, Column, Container, ElevatedButton, Image, ImageFit, ImageRepeat,
                  icons, MainAxisAlignment, Margin, OutlinedButton, Padding, Row, Text,
                  TextAlign, TextButton, TextThemeStyle, colors)

from screens.graphic.abstract_pages import Page
from utils.constants import ABSOLUTE_IMAGES_PATH

LOGO_LETTERS_IMAGE_PATH = ABSOLUTE_IMAGES_PATH + "/logo-removedbg-only-letters.png"
PAGE_IMAGE = ABSOLUTE_IMAGES_PATH + "/praia-1.jpg"


class InicioDeslogado(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
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
                bgcolor=colors.TEAL_ACCENT_700,
                actions=[
                    Container(
                        content=Row(
                            [
                                TextButton(
                                    "Buscar imóveis",
                                    on_click=self.__listagem_imoveis,
                                ),
                                OutlinedButton(
                                    "Entrar",
                                    icon=icons.PERSON_2_OUTLINED,
                                    on_click=self.__cadastro_login,
                                )
                            ],
                            spacing=48,
                            alignment=MainAxisAlignment.START,
                        ),
                        margin=Margin(48, 0, 48, 0)
                    )

                ]
            ),
            # Corpo da página
            Column(
                [
                    Row(
                        [
                            Image(
                                src=PAGE_IMAGE,
                                fit=ImageFit.FILL,
                                repeat=ImageRepeat.NO_REPEAT,
                                height=800,
                                expand=3,
                            ),
                            Column(
                                [
                                    Column(
                                        [
                                            Text(
                                                "Venha conhecer a melhor cidade para passar suas férias!",  # noqa
                                                style=TextThemeStyle.HEADLINE_SMALL,
                                                text_align=TextAlign.LEFT,
                                            ),
                                            Text(
                                                """
Chega de passar horas procurando onde você e sua familia vão ficar.
Chega de preocupação com a segurança do local.

Deixe que a gente cuida disso para você!
                                                """
                                            ),
                                            Text(
                                                "Apenas curtam suas férias!",
                                                style=TextThemeStyle.TITLE_MEDIUM,
                                            ),
                                            Row(
                                                [
                                                    ElevatedButton(
                                                        "Buscar imóveis",
                                                        on_click=self.__listagem_imoveis,
                                                    ),
                                                ],
                                        alignment=MainAxisAlignment.START,
                                    ),
                                        ],
                                        spacing=16,
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "Já mora em florianópolis e quer alugar?",  # noqa
                                                style=TextThemeStyle.HEADLINE_SMALL,
                                                text_align=TextAlign.LEFT,
                                            ),
                                            Text(
                                                """
Chega de burrocracia para alugar seu imóvel.

Nós trabalhamos para você!
                                                """
                                            ),
                                            Text(
                                                "Traga seu imóvel!",
                                                style=TextThemeStyle.TITLE_MEDIUM,
                                            ),
                                            Row(
                                                [
                                                    ElevatedButton(
                                                        "Cadastrar meus imóveis",
                                                        on_click=self.__cadastro_login,
                                                    ),
                                                ],
                                                alignment=MainAxisAlignment.START,
                                            ),
                                        ],
                                        spacing=16,
                                    )

                                ],  # EndColumnContent
                                expand=2,
                                height=800,
                                alignment=MainAxisAlignment.SPACE_EVENLY,
                            )
                        ],
                        spacing=48,
                        alignment=MainAxisAlignment.CENTER,
                    )
                ],
                alignment=MainAxisAlignment.START,
                height=1000,
            ),  # EndColumn
        ]

    def preencher_payload(self, event, comando) -> None:
        self.payload = {"comando": comando}

    def __listagem_imoveis(self, event) -> None:
        self.preencher_payload(event, "1")

    def __cadastro_login(self, event) -> None:
        self.preencher_payload(event, "2")
