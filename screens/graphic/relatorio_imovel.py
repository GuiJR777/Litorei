import re
from flet import (
    alignment,
    border,
    border_radius,
    colors,
    Column,
    Container,
    DataCell,
    DataColumn,
    DataRow,
    DataTable,
    Row,
    Text,
)


class ImovelRelatorioCard:
    def __init__(self, identificador, titulo, preco, alugueis) -> None:
        self.__identificador = identificador
        self.__titulo = titulo
        self.__preco = preco
        self.__alugueis = alugueis
        self.__ganho_total = 0

    @property
    def ganho_total(self):
        return self.__ganho_total

    def exibir(self) -> Container:
        alugueis = DataTable(
            columns=[
                DataColumn(
                    Text("Data da reserva"),
                ),
                DataColumn(
                    Text("Número de dias"),
                ),
                DataColumn(
                    Text("Nome do locatário"),
                ),
                DataColumn(
                    Text("Total do imóvel"),
                ),
            ],  # EndColumns
        )

        for aluguel in self.__alugueis:
            preco_total = float(self.__preco) * float(aluguel["diarias"])
            self.__ganho_total += preco_total
            alugueis.rows.append(
                DataRow(
                    cells=[
                        DataCell(
                            Text(aluguel["data_inicio"]),
                        ),
                        DataCell(
                            Text(aluguel["diarias"]),
                        ),
                        DataCell(
                            Text(aluguel["locatario"]),
                        ),
                        DataCell(
                            Text(
                                f"R$ {preco_total}",
                            ),
                        ),
                    ]
                )
            )

        return Container(
            content=Column(
                [
                    Row(
                        [
                            Text(f"Imóvel: {self.__identificador}"),
                        ]
                    ),
                    Row(
                        [
                            Text(f"Titulo: {self.__titulo}"),
                        ]
                    ),
                    Row(
                        [
                            Text(f"Preço: R$ {self.__preco}"),
                        ]
                    ),
                    alugueis,
                ]
            ),
            alignment=alignment.center,
            border=border.all(1, colors.PRIMARY),
            border_radius=border_radius.all(16),
            padding=48,
            col={"sm": 12, "md": 12, "xl": 12},
        )
