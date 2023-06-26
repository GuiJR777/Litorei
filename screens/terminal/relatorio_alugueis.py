from screens.terminal.abstract_screen import Screen


class RelatorioAlugueis(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Relatório de aluguéis"
        self.__relatorio_data = None

    def entrada(self, data) -> None:
        self.__relatorio_data = data
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> None:
        for imovel_id, imovel_data in self.__relatorio_data.items():
            self.show_info(
                f"""
{'-' * 30}
IMOVEL            | {imovel_id}
TITULO            | {imovel_data['titulo']}
PREÇO             | {imovel_data['preco']}

                """
            )
            for aluguel in imovel_data["alugueis"]:
                self.show_info(
                    f"""
DATA DA RESERVA   | {aluguel['data_inicio']}
NUMERO DE DIAS    | {aluguel['diarias']}
NOME DO LOCATARIO | {aluguel['locatario']}

TOTAL DO IMOVEL   | R$ {float(imovel_data['preco']) * float(aluguel['diarias'])}
{'-' * 30}
                    """
                )
        valor_total = 0

        for imovel in self.__relatorio_data.values():
            for aluguel in imovel["alugueis"]:
                valor_total += float(imovel["preco"]) * float(
                    aluguel["diarias"]
                )

        self.show_info(
            f"""

TOTAL NESSE ANO  | R$ {valor_total}

{'-' * 30}
            """
        )

        return self.selecionar(
            {
                "1": "Voltar",
            }
        )
