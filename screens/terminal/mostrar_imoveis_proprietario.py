from screens.terminal.abstract_screen import Screen


class MostrarImoveisProprietario(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Seus Imóveis"
        self.__imoveis_data = None

    def entrada(self, imoveis_data) -> None:
        self.__imoveis_data = imoveis_data
        self.clear_terminal()
        self.show_titulo()

    def campos(self):
        opcoes = {}

        for index, imovel in enumerate(self.__imoveis_data):
            opcoes[str(index + 1)] = f"{imovel['titulo']} - {imovel['preco']}"

        opcoes[str(len(opcoes) + 1)] = "Voltar"

        self.show_info("Selecione um imóvel para ver mais detalhes ou voltar")
        return self.selecionar(opcoes)
