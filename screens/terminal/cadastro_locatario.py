from screens.terminal.abstract_screen import Screen
from screens.enumerators import TiposDeRespostas
from screens.terminal.exceptions import UsuarioQuerVoltarException


class CadastroLocatario(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Tela de Cadastro"

    def entrada(self) -> None:
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> None:
        try:
            return {
                "nome": self.questionar(
                    "Qual é o seu nome?", TiposDeRespostas.TEXTO
                ),
                "email": self.questionar(
                    "Qual é o seu email?", TiposDeRespostas.EMAIL
                ),
                "senha": self.questionar(
                    "Qual é a sua senha?", TiposDeRespostas.SENHA
                ),
                "documento": self.questionar(
                    "Qual é o seu CPF?", TiposDeRespostas.NUMERICO
                ),
                "telefone": self.questionar(
                    "Qual é o seu telefone?", TiposDeRespostas.NUMERICO
                ),
            }
        except UsuarioQuerVoltarException:
            return None
