from screens.terminal.abstract_screen import Screen


class Welcome(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Bem vindo"

    def entrada(self) -> None:
        self.clear_terminal()
        self.digitar_na_tela("Bem vindo ao ...")
        self.show_success(
            """
 _       _  _                       _
| |     (_)| |                     (_)
| |      _ | |_   ___   _ __   ___  _
| |     | || __| / _ \ | '__| / _ \| |
| |____ | || |_ | (_) || |   |  __/| |
|______||_| \__| \___/ |_|    \___||_|


            """,
        )
        self.clear_terminal(2)

    def campos(self) -> None:
        pass
