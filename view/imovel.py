from controller.enumerators import ComandoUsuario
from screens.terminal.enumerators import Telas
from view.abstract_view import View


class ImovelView(View):
    def __init__(self, screen_manager) -> None:
        self.screen_manager = screen_manager

    def listar_imoveis(self, imoveis_data: list[dict]) -> None:
        self.screen_manager.trocar_de_tela(
            Telas.LISTAGEM_IMOVEIS, imoveis_data=imoveis_data
        )
        resposta = self.screen_manager.esperar_comando_usuario()

        if int(resposta) == len(imoveis_data) + 1:
            return ComandoUsuario.VOLTAR
        return int(resposta) - 1

    def cadastrar(self):
        self.screen_manager.trocar_de_tela(Telas.CADASTRO_IMOVEL)
        resposta = self.screen_manager.esperar_comando_usuario()

        if not resposta:
            return ComandoUsuario.VOLTAR

        return resposta
