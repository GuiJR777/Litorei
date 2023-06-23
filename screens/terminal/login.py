from screens.terminal.abstract_screen import Screen
from screens.enumerators import TiposDeRespostas
from screens.terminal.exceptions import UsuarioQuerVoltarException


class Login(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Login"

    def entrada(self) -> None:
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> None:
        try:
            return {
                "email": self.questionar(
                    "Digite seu email", TiposDeRespostas.EMAIL
                ),
                "senha": self.questionar(
                    "Digite sua senha", TiposDeRespostas.SENHA
                ),
            }
        except UsuarioQuerVoltarException:
            return None
