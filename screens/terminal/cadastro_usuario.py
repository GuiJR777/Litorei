from screens.terminal.abstract_screen import Screen


class CadastroUsuario(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Tela de Cadastro"

    def entrada(self) -> None:
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> None:
        return self.selecionar(
            {
                "1": "Estou procurando um imóvel",
                "2": "Quero anunciar meus imóveis",
                "3": "Voltar",
            }
        )
