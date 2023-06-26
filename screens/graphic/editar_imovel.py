# https://flet.dev/docs/
from flet import (
    AppBar,
    Column,
    Dropdown,
    dropdown,
    ElevatedButton,
    IconButton,
    Image,
    ImageFit,
    ImageRepeat,
    KeyboardType,
    MainAxisAlignment,
    Row,
    Text,
    TextAlign,
    TextField,
    TextThemeStyle,
    icons,
)

from screens.graphic.abstract_pages import Page
from utils.constants import ABSOLUTE_IMAGES_PATH

LOGO_LETTERS_IMAGE_PATH = (
    ABSOLUTE_IMAGES_PATH + "/logo-removedbg-only-letters.png"
)


class EditarImovel(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
        # Form fields
        imovel_data = self.data["data"]
        self.titulo = TextField(
            label="Título",
            hint_text="De um título para o seu imóvel",
            value=imovel_data["titulo"],
        )
        self.endereco = TextField(
            label="Endereço",
            hint_text="Digite seu endereço completo",
            keyboard_type=KeyboardType.STREET_ADDRESS,
            multiline=True,
            value=imovel_data["endereco"],
        )
        self.preco = Row(
            [
                Text("R$"),
                TextField(
                    label="Preço",
                    hint_text="Qual o preço da diaria sem centavos?",
                    width=100,
                    value=int(imovel_data["preco"]),
                    suffix_text=",00",
                    keyboard_type=KeyboardType.NUMBER,
                    text_align=TextAlign.RIGHT,
                ),
                Text("por dia."),
            ]
        )
        self.info = TextField(
            label="Detalhes",
            hint_text="Dê mais detalhes sobre seu imóvel",
            multiline=True,
            value=imovel_data["informacoes"],
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
                                "Cadastro de Imóvel",
                                style=TextThemeStyle.TITLE_LARGE,
                            ),
                            self.titulo,
                            self.preco,
                            self.endereco,
                            self.info,
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
        preco = str(int(self.preco.controls[1].value)).replace(",", ".")

        self.preencher_payload(
            event,
            {
                "titulo": self.titulo.value,
                "endereco": self.endereco.value,
                "preco": self.__remove_non_digits(preco),
                "informacoes": self.info.value,
            },
        )

    def __voltar(self, event) -> None:
        self.preencher_payload(event, {"comando": None})

    @staticmethod
    def __remove_non_digits(string: str) -> str:
        return "".join([char for char in string if char.isdigit()])
