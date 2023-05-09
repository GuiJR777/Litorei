from screens.terminal.abstract_screen import Screen


class Agradecimento(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Tela Agradecimento"

    def entrada(self):
        self.clear_terminal()
        self.digitar_na_tela(
            "Obrigado por acessar o Litorei!! Espero ve-lo em breve!!"
        )
        exit()

    def campos(self) -> None:
        pass
