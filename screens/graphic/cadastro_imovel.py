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
    TextField,
    TextThemeStyle,
    icons,
)

from screens.graphic.abstract_pages import Page
from utils.constants import ABSOLUTE_IMAGES_PATH

LOGO_LETTERS_IMAGE_PATH = (
    ABSOLUTE_IMAGES_PATH + "/logo-removedbg-only-letters.png"
)


class CadastroImovel(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
        # Form fields
        self.titulo = TextField(
            label="Título",
            hint_text="De um título para o seu imóvel"
        )
        self.endereco = TextField(
            label="Endereço",
            hint_text="Digite o nome da rua e número do imóvel",
            keyboard_type=KeyboardType.STREET_ADDRESS
        )
        self.bairro = TextField(
            label="Bairro",
            hint_text="Em que bairro fica o imóvel?"
        )
        self.cep = TextField(
            label="CEP",
            hint_text="Qual o cep do imóvel?",
            keyboard_type=KeyboardType.NUMBER
        )
        self.cidade = Dropdown(
            label="Cidade",
            hint_text="Qual a cidade do seu imóvel?",
            options=[
                dropdown.Option("Florianópolis"),
                dropdown.Option("São José"),
                dropdown.Option("Palhoça"),
            ],
        )
        self.preco = Row(
            [
                Text("R$"),
                TextField(
                    label="Preço",
                    hint_text="Qual o preço da diaria sem centavos?",
                    width=100,
                    value="0",
                    suffix_text=",00",
                    keyboard_type=KeyboardType.NUMBER
                ),
                Text("por dia.")
            ]
        )
        self.info = TextField(
            label="Detalhes",
            hint_text="Dê mais detalhes sobre seu imóvel",
            multiline=True,
            value="""
Quantos quartos?
Garagem?
Piscina?
Perto do que?
Algum diferencial?
            """
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
                            self.endereco,
                            self.bairro,
                            self.cep,
                            self.cidade,
                            self.preco,
                            self.info,
                            ElevatedButton(
                                "Cadastrar",
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
        endereco_completo = (
            f"{self.endereco.value}, {self.bairro.value}, {self.cidade.value} - {self.cep.value} - SC, Brasil"  # noqa
        )
        preco = self.preco.controls[1].value.replace(",", ".")

        self.preencher_payload(
            event,
            {
                "titulo": self.titulo.value,
                "endereco": endereco_completo,
                "preco": self.__remove_non_digits(preco),
                "informacoes": self.info.value,
            },
        )

    def __voltar(self, event) -> None:
        self.preencher_payload(event, {"comando": None})

    @staticmethod
    def __remove_non_digits(string: str) -> str:
        return "".join([char for char in string if char.isdigit()])
