from screens.terminal.abstract_screen import Screen
from screens.terminal.enumerators import TiposDeRespostas
from screens.terminal.exceptions import UsuarioQuerVoltarException


class CadastroProprietario(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Tela de Cadastro"

    def entrada(self) -> None:
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> None:
        try:
            questionario = {
                "nome": self.questionar(
                    "Qual é o seu nome?", TiposDeRespostas.TEXTO
                ),
                "email": self.questionar(
                    "Qual é o seu email?", TiposDeRespostas.EMAIL
                ),
                "senha": self.questionar(
                    "Qual é a sua senha?", TiposDeRespostas.SENHA
                ),
                "telefone": self.questionar(
                    "Qual é o seu telefone?", TiposDeRespostas.NUMERICO
                ),
            }
            e_PJ = self.questionar(
                    "Você é pessoa juridica?", TiposDeRespostas.SIM_OU_NAO
            )

            if e_PJ == "s":
                questionario["tipo"] = "pj"
                questionario["documento"] = self.questionar(
                    "Qual é o seu CNPJ?", TiposDeRespostas.NUMERICO
                )
            else:
                questionario["tipo"] = "pf"
                questionario["documento"] = self.questionar(
                    "Qual é seu CPF?", TiposDeRespostas.NUMERICO
                )
            return questionario

        except UsuarioQuerVoltarException:
            return None
