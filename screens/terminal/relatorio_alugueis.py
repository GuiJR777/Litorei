from screens.terminal.abstract_screen import Screen


class RelatorioAlugueis(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Relatório de aluguéis"
        self.__relatorio_data = None

    def entrada(self, relatorio_data) -> None:
        self.__relatorio_data = relatorio_data
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> None:
        for imovel in self.__relatorio_data:
            self.show_info(
                f"""
{'-' * 30}
IMOVEL            | {imovel['identificador']}
TITULO            | {imovel['titulo']}
PREÇO             | {imovel['preco']}

                """
            )
            for aluguel in imovel["alugueis"]:
                self.show_info(
                    f"""
DATA DA RESERVA   | {aluguel['data_reserva']}
NUMERO DE DIAS    | {aluguel['numero_de_dias']}
NOME DO LOCATARIO | {aluguel['locatario']}

TOTAL DO IMOVEL   | {float(imovel['preco']) * float(aluguel['numero_de_dias'])}
{'-' * 30}
                    """
                )
        valor_total = 0

        for imovel in self.__relatorio_data:
            for aluguel in imovel["alugueis"]:
                valor_total += float(imovel["preco"]) * float(
                    aluguel["numero_de_dias"]
                )

        self.show_info(
            f"""

TOTAL            | {valor_total}

{'-' * 30}
            """
        )

        return self.selecionar(
            {
                "1": "Voltar",
            }
        )
