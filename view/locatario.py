from screens.terminal.enumerators import Telas
from view.abstract_view import View


class LocatarioView(View):
    def __init__(self) -> None:
        super().__init__()

    def cadastrar(self) -> dict:
        self.screen_manager.trocar_de_tela(Telas.CADASTRO_LOCATARIO)
        resposta = self.screen_manager.esperar_comando_usuario()

        return resposta

    def iniciar(self) -> None:
        pass
