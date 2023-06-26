from controller.enumerators import ComandoUsuario
from screens.enumerators import Telas
from view.abstract_view import View


class ImovelView(View):
    def __init__(self, screen_manager) -> None:
        self.screen_manager = screen_manager

    def listar_imoveis(self, imoveis_data: list[dict]) -> None:
        self.screen_manager.trocar_de_tela(
            Telas.LISTAGEM_IMOVEIS, data={"imoveis": imoveis_data}
        )
        resposta = self.screen_manager.esperar_comando_usuario()

        if int(resposta) == len(imoveis_data) + 1:
            return ComandoUsuario.VOLTAR
        return int(resposta) - 1

    def erro_listar_imoveis(self) -> None:
        self.screen_manager.feedback_erro("Nenhum imóvel cadastrado")

    def mostrar_imovel(self, imovel_data: dict) -> None:
        self.screen_manager.trocar_de_tela(
            Telas.MOSTRAR_IMOVEL, data={"data": imovel_data}
        )
        resposta = self.screen_manager.esperar_comando_usuario()

        match resposta:
            case "1":
                return ComandoUsuario.ALUGAR_IMOVEL
            case "2":
                return ComandoUsuario.VOLTAR

    def cadastrar(self):
        self.screen_manager.trocar_de_tela(Telas.CADASTRO_IMOVEL)
        resposta = self.screen_manager.esperar_comando_usuario()

        if not resposta:
            return ComandoUsuario.VOLTAR

        return resposta
