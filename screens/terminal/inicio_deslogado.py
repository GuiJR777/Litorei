from screens.terminal.abstract_screen import Screen


class InicioDeslogado(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Bem vindo!"

    def entrada(self) -> None:
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> str:
        return self.selecionar(
            {
                "1": "Ver imóveis",
                "2": "Login",
                "3": "Sair",
            }
        )
