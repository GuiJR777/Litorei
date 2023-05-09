from screens.terminal.abstract_screen import Screen


class CadastroLogin(Screen):
    def __init_(self) -> None:
        super().__init__()
        self.titulo = "Cadastro e Login"

    def entrada(self) -> None:
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> str:
        return self.selecionar(
            {
                "1": "Cadastrar-se",
                "2": "Logar",
                "3": "Voltar",
            }
        )
