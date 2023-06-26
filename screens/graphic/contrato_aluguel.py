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


class ContratoAluguel(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
        imovel_data = self.data

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
            ),
            # Fim do menu da parte superior
            Row(
                [
                    Column(
                        [
                            Text(
                                "Seu contrato de aluguel",
                                style=TextThemeStyle.TITLE_LARGE,
                            ),
                            Text(
                                f"Titulo: {imovel_data['titulo']}",
                            ),
                            Text(
                                f"Proprietário: {imovel_data['proprietario']}",
                            ),
                            Text(
                                f"Número de diarias: {imovel_data['diarias']}",
                            ),
                            Text(
                                f"Valor: R$ {imovel_data['preco']}",
                            ),
                            Text(
                                f"Dia de checkin: {imovel_data['checkin']}",
                            ),
                            Text(
                                f"Endereço: {imovel_data['endereco']}",
                            ),
                            ElevatedButton(
                                "Devolver imóvel",
                                on_click=self.__devolver_imovel,
                                bgcolor="red",
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        width=600,
                    ),  # EndColumn
                    Column(
                        [
                            Image(
                                src="https://source.unsplash.com/600x600/?house",  # noqa
                                fit=ImageFit.CONTAIN,
                                repeat=ImageRepeat.NO_REPEAT,
                                height=600,
                                width=600,
                            ),
                        ]
                    ),  # EndColumn
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        ]

    def preencher_payload(self, event, content: dict) -> None:
        self.payload = content

    def __devolver_imovel(self, event) -> None:
        self.preencher_payload(event, {"comando": "1"})

    def __voltar(self, event) -> None:
        self.preencher_payload(event, {"comando": "2"})
