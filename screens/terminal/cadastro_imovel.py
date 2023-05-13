from screens.terminal.abstract_screen import Screen
from screens.terminal.enumerators import TiposDeRespostas
from screens.terminal.exceptions import UsuarioQuerVoltarException


class CadastroImovel(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Tela de Cadastro de Imóvel"

    def entrada(self) -> None:
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> None:
        try:
            return {
                "titulo": self.questionar(
                    "De um titulo para anunciar seu imovel", TiposDeRespostas.TEXTO
                ),
                "endereco": self.questionar(
                    "Qual é o endereco do seu imovel?", TiposDeRespostas.TEXTO
                ),
                "preco": self.questionar(
                    "Qual é o preco da diaria do seu imovel?", TiposDeRespostas.NUMERICO
                ),
                "informacoes": self.questionar(
                    "De informacoes sobre seu imovel... ", TiposDeRespostas.TEXTO
                )
            }
        except UsuarioQuerVoltarException:
            return None
