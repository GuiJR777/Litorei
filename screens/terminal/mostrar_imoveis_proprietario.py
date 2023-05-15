from screens.terminal.abstract_screen import Screen


class MostrarImoveisProprietario(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Seus Imóveis"

    def entrada(self, imoveis_data) -> None:
        self.clear_terminal()
        self.show_titulo()

    def campos(self):
        pass
        #listar imoveis do proprietario    
