from screens.terminal.screen import Screen


class Welcome(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.add_opcao(1, self.__tela_imoveis)
        self.add_opcao(2, self.__tela_login)

    def entrada(self) -> None:
        self.clear_terminal()

        self.__show_welcome()

        self.clear_terminal(2)

        self.__show_options()

    def __show_welcome(self) -> None:
        self.digitar_na_tela("Bem vindo ao Litorei!")
        self.show(
            """
 _       _  _                       _
| |     (_)| |                     (_)
| |      _ | |_   ___   _ __   ___  _
| |     | || __| / _ \ | '__| / _ \| |
| |____ | || |_ | (_) || |   |  __/| |
|______||_| \__| \___/ |_|    \___||_|


            """,
        )

    def __show_options(self) -> None:
        self.show("Selecione uma opção:")
        self.show_opcao(1, "Ver imóveis")
        self.show_opcao(2, "Login")
        self.show_opcao(0, "Sair")

        self.__get_option()

    def __get_option(self) -> None:
        opcao = input("Opção: ")

        if not self.opcao_valida(opcao):
            self.show_error("Opção inválida!")
            self.clear_terminal(1)
            self.__show_options()

        self.clear_terminal(1)
        self.mapa_opcoes[int(opcao)]()

    def __tela_imoveis(self) -> None:
        self.show("Tela de imóveis")
        input("Pressione enter para voltar...")
        self.clear_terminal(1)
        self.__show_options()

    def __tela_login(self) -> None:
        self.show("Tela de login")
        input("Pressione enter para voltar...")
        self.clear_terminal(1)
        self.__show_options()
