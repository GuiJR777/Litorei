from screens.terminal.abstract_screen import Screen


class MostrarImovel(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Imóvel"
        self.__imovel_data = None
        self.__eh_locatario = None

    def entrada(self, imovel_data, eh_locatario: bool = True) -> None:
        self.__imovel_data = imovel_data
        self.__eh_locatario = eh_locatario
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> None:
        self.show_info(
            f"""
{'-' * 30}
{self.__imovel_data["titulo"].capitalize()}

Diaria de R$ {self.__imovel_data["preco"]}

{'-' * 30}

Descrição:
{self.__imovel_data["informacoes"]}

{'-' * 30}

Endereço:
{self.__imovel_data["endereco"]}
{'-' * 30}
            """
        )

        if self.__eh_locatario:
            return self.selecionar(
                {
                    "1": "Alugar",
                    "2": "Voltar",
                }
            )
        else:
            return self.selecionar(
                {
                    "1": "Editar",
                    "2": "Excluir",
                    "3": "Voltar",
                }
            )
