from screens.terminal.abstract_screen import Screen
from screens.terminal.enumerators import TiposDeRespostas


class Login(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Login"

    def entrada(self) -> None:
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> None:
        return {
            "email": self.questionar(
                "Digite seu email", TiposDeRespostas.EMAIL
            ),
            "senha": self.questionar(
                "Digite sua senha", TiposDeRespostas.SENHA
            ),
        }
