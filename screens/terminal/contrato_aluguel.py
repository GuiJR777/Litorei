from screens.terminal.abstract_screen import Screen


class ContratoAluguel(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Tela de Contrato"
        self.__contrato_data = None

    def entrada(self, contrato_data) -> None:
        self.__contrato_data = contrato_data
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> None:
        self.show_info(
            f"""
{'-' * 30}
Aluguel
{'-' * 30}

Propriedade: {self.__contrato_data["titulo"]}
Proprietário: {self.__contrato_data["proprietario"]}
Diaría: {self.__contrato_data["preco"]}
Numero de diarias: {self.__contrato_data["diarias"]}
Endereço: {self.__contrato_data["endereco"]}
Data de check-in: {self.__contrato_data["checkin"]}
{'-' * 30}

            """
        )

        return self.selecionar(
            {
                "1": "Devolver imóvel",
                "2": "Voltar",
            },
        )
