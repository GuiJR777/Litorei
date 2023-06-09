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
    TextField,
    TextThemeStyle,
    icons,
)

from screens.graphic.abstract_pages import Page
from utils.constants import ABSOLUTE_IMAGES_PATH

LOGO_LETTERS_IMAGE_PATH = (
    ABSOLUTE_IMAGES_PATH + "/logo-removedbg-only-letters.png"
)


class EditarPerfilProprietario(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
        # Form fields
        self.nome = TextField(
            label="Nome",
            hint_text="Seu nome",
            value=self.data.get("nome"),
        )
        self.email = TextField(
            label="Email",
            hint_text="seu.nome@email.com",
            value=self.data.get("email"),
        )
        self.documento = TextField(
            label="Documento",
            hint_text="Documento",
            value=self.data.get("documento"),
        )
        self.telefone = TextField(
            label="Telefone",
            hint_text="Telefone",
            value=self.data.get("telefone"),
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
                #
            ),
            # Fim do menu da parte superior
            Row(
                [
                    Column(
                        [
                            Text(
                                "Editar perfil",
                                style=TextThemeStyle.TITLE_LARGE,
                            ),
                            self.nome,
                            self.documento,
                            self.telefone,
                            self.email,
                            ElevatedButton(
                                "Salvar",
                                on_click=self.__submit_form,  # noqa
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

    def __submit_form(self, event) -> None:
        self.preencher_payload(
            event,
            {
                "nome": self.nome.value,
                "email": self.email.value,
                "documento": self.__remove_non_digits(self.documento.value),
                "telefone": self.__remove_non_digits(self.telefone.value),
            },
        )

    def __voltar(self, event) -> None:
        self.preencher_payload(event, {"comando": None})

    @staticmethod
    def __remove_non_digits(string: str) -> str:
        return "".join([char for char in string if char.isdigit()])
