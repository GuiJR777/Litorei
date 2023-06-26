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
from screens.graphic.tipo_usuario import TipoUsuario
from utils.constants import ABSOLUTE_IMAGES_PATH


LOGO_LETTERS_IMAGE_PATH = (
    ABSOLUTE_IMAGES_PATH + "/logo-removedbg-only-letters.png"
)


class MostrarImovel(Page):
    def __init__(self, route) -> None:
        super().__init__(route)

    def exibir_pagina(self) -> None:
        botoes = Row()
        match self.usuario_logado:
            case TipoUsuario.PROPRIETARIO:
                botoes.controls = [
                    ElevatedButton(
                        "Editar",
                        icon=icons.EDIT,
                        on_click=self.__primeiro_comando,
                    ),
                    ElevatedButton(
                        "Excluir",
                        icon=icons.DELETE,
                        on_click=self.__deletar_imovel,
                    ),
                ]
            case _:
                botoes.controls = [
                    ElevatedButton(
                        "Alugar",
                        icon=icons.EDIT,
                        on_click=self.__primeiro_comando,
                        bgcolor="green",
                    ),
                ]

        imovel_data = self.data["data"]

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
                                imovel_data["titulo"],
                                style=TextThemeStyle.TITLE_LARGE,
                            ),
                            Text(
                                f"Proprietário: {imovel_data['proprietario']}",
                            ),
                            Image(
                                src="https://source.unsplash.com/600x600/?house",  # noqa
                                fit=ImageFit.CONTAIN,
                                repeat=ImageRepeat.NO_REPEAT,
                                height=600,
                                width=600,
                            ),
                            Text(
                                f"Valor: R$ {imovel_data['preco']}",
                            ),
                            Text(
                                f"Endereço: {imovel_data['endereco']}",
                            ),
                            Text(
                                imovel_data["informacoes"],
                            ),
                            botoes,
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    )  # EndColumn
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        ]

    def preencher_payload(self, event, content: dict) -> None:
        self.payload = content

    def __primeiro_comando(self, event) -> None:
        self.preencher_payload(event, {"comando": "1"})

    def __deletar_imovel(self, event) -> None:
        self.preencher_payload(event, {"comando": "2"})

    def __voltar(self, event) -> None:
        comando = (
            "3" if self.usuario_logado == TipoUsuario.PROPRIETARIO else "2"
        )  # noqa
        self.preencher_payload(event, {"comando": comando})
