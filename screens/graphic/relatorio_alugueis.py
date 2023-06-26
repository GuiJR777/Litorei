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
    TextField,
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

    def exibir_pagina(self) -> None:
        cards = ResponsiveRow(alignment=MainAxisAlignment.CENTER)
        valor_total = 0

        for imovel_id, imovel_data in self.data.items():
            card = ImovelRelatorioCard(
                imovel_id,
                imovel_data["titulo"],
                imovel_data["preco"],
                imovel_data["alugueis"],
            )
            valor_total += card.ganho_total
            cards.controls.append(card.exibir())

        ganhos_totais = Row(
            [
                Text(
                    "Ganhos totais: R$ ",
                    style=TextThemeStyle.TITLE_LARGE,
                ),
                TextField(
                    label="Ganhos totais",
                    read_only=True,
                    value=valor_total,
                )
            ]
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
