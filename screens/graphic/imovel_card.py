from flet import (
    alignment,
    border,
    border_radius,
    colors,
    Column,
    Container,
    Image,
    ImageFit,
    ImageRepeat,
    MainAxisAlignment,
    Row,
    Text,
    TextAlign,
    TextButton,
)


class ImovelCard:
    def __init__(self, identificador, titulo, preco, index) -> None:
        self.__identificador = identificador
        self.__titulo = titulo
        self.__preco = preco
        self.__index = index

    @property
    def identificador(self) -> str:
        return self.__identificador

    def exibir(self, action) -> Container:
        return Container(
            content=Column(
                [
                    Row(
                        [
                            Image(
                                src="https://source.unsplash.com/300x300/?house",  # noqa
                                fit=ImageFit.CONTAIN,
                                repeat=ImageRepeat.NO_REPEAT,
                                height=200,
                                width=284,
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),  # EndRowImage
                    Row(
                        [
                            TextButton(
                                text=self.__titulo,
                                on_click=action,
                                tooltip=f"Ver detalhes do imóvel {int(self.__index) + 1}",  # noqa
                            )
                        ]
                    ),  # EndRowTitle
                    Row(
                        [
                            Text(
                                f"R$ {self.__preco}",
                                text_align=TextAlign.RIGHT,
                            )
                        ],
                        alignment=MainAxisAlignment.END,
                    ),  # EndRowPrice
                ],
            ),
            alignment=alignment.center,
            border=border.all(1, colors.PRIMARY),
            border_radius=border_radius.all(16),
            col={"sm": 6, "md": 4, "xl": 3},
            height=300,
            padding=16,
            width=300,
        )
