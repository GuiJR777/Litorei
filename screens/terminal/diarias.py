from screens.terminal.abstract_screen import Screen
from screens.enumerators import TiposDeRespostas


class Diarias(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Confirmação de aluguel"

    def entrada(self) -> None:
        self.clear_terminal()
        self.show_titulo()

    def campos(self):
        return self.questionar(
            "Quantos dias deseja ficar no imovel? (digite 0 caso deseje desistir)",
            TiposDeRespostas.NUMERICO,
        )
