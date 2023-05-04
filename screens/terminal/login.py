from screens.terminal.screen import Screen
from screens.terminal.cadastro_usuario import CadastroUsuario
from screens.terminal.logar import Logar


class Login(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Tela de Login"
        self.add_opcao(1, self.__tela_cadastro)
        self.add_opcao(2, self.__tela_login)
        self.add_opcao(3, self.voltar_para_tela_anterior)

    def entrada(self) -> None:
        self.show_titulo()
        self.__show_options()

    def __show_options(self) -> None:
        self.show("Selecione uma opção:")
        self.show_opcao(1, "Cadastrar")
        self.show_opcao(2, "Login")
        self.show_opcao(3, "Voltar")

        self.get_opcao()()

    def __tela_cadastro(self) -> None:
        cadastro = CadastroUsuario()
        self.trocar_de_tela(cadastro)

    def __tela_login(self) -> None:
        logar = Logar()
        self.trocar_de_tela(logar)
