# https://flet.dev/docs/
from flet import (
    AppBar,
    Column,
    ElevatedButton,
    IconButton,
    Image,
    ImageFit,
    ImageRepeat,
    KeyboardType,
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


class Diarias(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
        self.numero_diarias = TextField(
            value=0,
            width=50,
            height=50,
            keyboard_type=KeyboardType.NUMBER,
        )
        self.valor_total = TextField(
            label="Valor Total",
            read_only=True,
            value=self.data["preco"] * self.numero_diarias.value,
        )

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
                                "Confirmar Aluguel",
                                style=TextThemeStyle.TITLE_LARGE,
                            ),
                            Text("Selecione a quantidade de diárias:"),
                            Row(
                                [
                                    IconButton(
                                        icon="remove",
                                        width=50,
                                        height=50,
                                        on_click=self.__remove_diarias_value,
                                    ),
                                    self.numero_diarias,
                                    IconButton(
                                        icon="add",
                                        width=50,
                                        height=50,
                                        on_click=self.__add_diarias_value,
                                    ),
                                ]
                            ),
                            Row(
                                [
                                    Text("Valor total: R$ "),
                                    self.valor_total,
                                ]
                            ),
                            ElevatedButton(
                                "Confirmar Aluguel",
                                on_click=self.__confirmar_aluguel,  # noqa
                                bgcolor="green",
                            ),  # EndButton
                        ],  # EndColumn
                        alignment=MainAxisAlignment.CENTER,
                        width=480,
                        height=800,
                    )  # EndColumn
                ],
                alignment=MainAxisAlignment.CENTER,
            ),  # EndRow
        ]  # EndControls

    def preencher_payload(self, event, content: dict) -> None:
        self.payload = content

    def __remove_diarias_value(self, event) -> None:
        self.numero_diarias.value -= 1

        if self.numero_diarias.value < 0:
            self.numero_diarias.value = 0

        self.valor_total.value = self.data["preco"] * self.numero_diarias.value

    def __add_diarias_value(self, event) -> None:
        self.numero_diarias.value += 1

        self.valor_total.value = self.data["preco"] * self.numero_diarias.value

    def __confirmar_aluguel(self, event) -> None:
        comando = str(self.numero_diarias.value)

        self.preencher_payload(event, {"comando": comando})

    def __voltar(self, event) -> None:
        self.preencher_payload(event, {"comando": "0"})
