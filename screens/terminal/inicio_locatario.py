from screens.terminal.abstract_screen import Screen


class InicioLocatario(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Bem vindo {name}!"

    def entrada(self, name) -> None:
        self.clear_terminal()
        self.titulo = self.titulo.format(name=name)
        self.show_titulo()

    def campos(self) -> str:
        return self.selecionar(
            {
                "1": "Ver imóveis",
                "2": "Ver perfil",
                "3": "Ver contratos",
                "4": "Deslogar",
            }
        )
