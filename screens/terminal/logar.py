from screens.terminal.enumerators import TiposDeRespostas
from screens.terminal.screen import Screen


class Logar(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Logar no sistema"

    def entrada(self) -> None:
        self.show_titulo()
        email = self.questionar("Digite seu email:", TiposDeRespostas.EMAIL)
        senha = self.questionar("Digite sua senha:", TiposDeRespostas.TEXTO)

        self.__validar_login(email, senha)

    def __validar_login(self, email: str, senha: str) -> None:
        # TODO: Trocar dados de login por dados do banco de dados
        email_valido, senha_valida = ("john@due", "123456")

        if email == email_valido and senha == senha_valida:
            self.show_success("Login realizado com sucesso!")
            input("Pressione enter para continuar...")
            self.clear_terminal(1)
            self.voltar_para_tela_anterior()
        else:
            self.show_error("Email ou senha inválidos!")
            input("Pressione enter para continuar...")
            self.clear_terminal(1)
            self.entrada()
