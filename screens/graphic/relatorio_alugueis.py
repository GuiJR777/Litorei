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
from screens.graphic.relatorio_imovel import ImovelRelatorioCard
from utils.constants import ABSOLUTE_IMAGES_PATH


LOGO_LETTERS_IMAGE_PATH = (
    ABSOLUTE_IMAGES_PATH + "/logo-removedbg-only-letters.png"
)


class RelatorioAlugueis(Page):
    def __init__(self, route) -> None:
        super().__init__(route)
        self.__valor_total = 0

    def exibir_pagina(self) -> None:
        cards = ResponsiveRow(alignment=MainAxisAlignment.CENTER)

        for imovel_id, imovel_data in self.data.items():
            card = ImovelRelatorioCard(
                imovel_id,
                imovel_data["titulo"],
                imovel_data["preco"],
                imovel_data["alugueis"],
            )
            self.__valor_total += card.ganho_total
            cards.controls.append(card.exibir())

        ganhos_totais = Text(
            f"Ganhos totais: R$ {self.__valor_total}",
            style=TextThemeStyle.TITLE_LARGE,
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
                                "Relatório de aluguéis",
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
            Row(
                [
                    Column(
                        [
                            ganhos_totais,
                        ]
                    )
                ]
            )
        ]

    def preencher_payload(self, event, content: dict) -> None:
        self.payload = content

    def __voltar(self, event) -> None:
        self.preencher_payload(
            event, {"comando": "1"}
        )
