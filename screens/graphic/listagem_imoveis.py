# https://flet.dev/docs/
from flet import (
    AppBar,
    Column,
    IconButton,
    Image,
    ImageFit,
    ImageRepeat,
    MainAxisAlignment,
    ResponsiveRow,
    Row,
    Text,
    TextThemeStyle,
    icons,
)

from screens.graphic.abstract_pages import Page
from utils.constants import ABSOLUTE_IMAGES_PATH
from screens.graphic.imovel_card import ImovelCard


LOGO_LETTERS_IMAGE_PATH = (
    ABSOLUTE_IMAGES_PATH + "/logo-removedbg-only-letters.png"
)


class ListagemImoveis(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
        cards = ResponsiveRow(alignment=MainAxisAlignment.CENTER)

        for index in range(len(self.data["imoveis"])):
            card = self.data["imoveis"][index]
            cards.controls.append(
                ImovelCard(
                    card["id"], card["titulo"], card["preco"], index
                ).exibir(self.__selecionar_imovel)
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
            ),
            # Fim do menu da parte superior
            Row(
                [
                    Column(
                        [
                            Text(
                                "Imóveis disponíveis",
                                style=TextThemeStyle.TITLE_LARGE,
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        height=120,
                    )  # EndColumn
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Column(
                [cards],
                alignment=MainAxisAlignment.CENTER,
            ),
        ]

    def preencher_payload(self, event, content: dict) -> None:
        self.payload = content

    def __voltar(self, event) -> None:
        self.preencher_payload(
            event, {"comando": len(self.data["imoveis"]) + 1}
        )

    def __selecionar_imovel(self, event) -> None:
        index = self.__remove_non_digits(event.control.tooltip)
        self.preencher_payload(event, {"comando": index})

    @staticmethod
    def __remove_non_digits(string: str) -> str:
        return "".join([char for char in string if char.isdigit()])
