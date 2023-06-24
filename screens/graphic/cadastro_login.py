# https://flet.dev/docs/
from flet import (
    AppBar,
    colors,
    Column,
    ElevatedButton,
    icons,
    IconButton,
    Image,
    ImageFit,
    ImageRepeat,
    MainAxisAlignment,
    Row,
    Text,
    TextButton,
    TextField,
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
        # Form fields
        self.email_field = TextField(
            label="Email", hint_text="seu.nome@email.com"
        )

        self.senha_field = TextField(
            label="Senha",
            hint_text="senha",
            password=True,
            can_reveal_password=True,
        )

        self.controls = [
            # Menu da parte superior
            AppBar(
                leading=IconButton(
                    icons.ARROW_BACK_IOS, on_click=self.__voltar
                ),  # noqa
                title=Image(
                    src=LOGO_LETTERS_IMAGE_PATH,
                    height=30,
                    fit=ImageFit.CONTAIN,
                    repeat=ImageRepeat.NO_REPEAT,
                ),
                bgcolor=colors.TEAL_ACCENT_700,
            ),
            # Fim do menu da parte superior
            Row(
                [
                    Column(
                        [
                            Image(
                                src=LOGO_LETTERS_IMAGE_PATH,
                                height=80,
                                fit=ImageFit.CONTAIN,
                                repeat=ImageRepeat.NO_REPEAT,
                            ),
                            self.email_field,
                            self.senha_field,
                            ElevatedButton(
                                "Entrar", on_click=self.__logar  # noqa
                            ),  # EndButton
                            Row(
                                [
                                    Text("Não possui cadastro ainda?"),
                                    TextButton(
                                        "Crie um aqui!",
                                        on_click=self.__cadastrar,
                                    ),
                                ]
                            ),
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

    def __cadastrar(self, event) -> None:
        self.preencher_payload(event, {"comando": "1"})

    def __logar(self, event) -> None:
        self.preencher_payload(
            event,
            {
                "comando": "2",
                "email": self.email_field.value,
                "senha": self.senha_field.value,
            },
        )

    def __voltar(self, event) -> None:
        self.preencher_payload(event, {"comando": "3"})
