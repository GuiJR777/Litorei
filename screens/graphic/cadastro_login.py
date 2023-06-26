# https://flet.dev/docs/
from flet import (
    AppBar,
    Column,
    Container,
    ElevatedButton,
    Image,
    ImageFit,
    ImageRepeat,
    Margin,
    MainAxisAlignment,
    Row,
    Text,
    TextButton,
    TextField,
    TextThemeStyle,
    colors,
)

from screens.graphic.abstract_pages import Page
from utils.constants import ABSOLUTE_IMAGES_PATH

LOGO_LETTERS_IMAGE_PATH = (
    ABSOLUTE_IMAGES_PATH + "/logo-removedbg-only-letters.png"
)


class CadastroLogin(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
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
                                    "Voltar",
                                    on_click=self.__voltar,
                                )
                            ],
                            spacing=48,
                            alignment=MainAxisAlignment.START,
                        ),
                        margin=Margin(48, 0, 48, 0),
                    )
                ],
            ),
            # Fim do menu da parte superior
            Column(
                [
                    Image(
                        src=LOGO_LETTERS_IMAGE_PATH,
                        height=80,
                        fit=ImageFit.CONTAIN,
                        repeat=ImageRepeat.NO_REPEAT,
                    ),
                    TextField(label="Email", hint_text="seu.nome@email.com"),
                    TextField(
                        label="Senha",
                        hint_text="password",
                        password=True,
                        can_reveal_password=True,
                    ),  # noqa
                    Text("Não possui cadastro? Crie um aqui!"),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        ]

    def preencher_payload(self, event) -> None:
        self.payload = {"comando": "entrar"}

    def __voltar(self, event) -> None:
        self.payload = {"comando": "3"}
