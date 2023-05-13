from controller.enumerators import ComandoUsuario
from screens.terminal.enumerators import Telas
from view.abstract_view import View


class ProprietarioView(View):
    def __init__(self, screen_manager) -> None:
        self.screen_manager = screen_manager

    def cadastrar(self):
        self.screen_manager.trocar_de_tela(Telas.CADASTRO_PROPRIETARIO)
        resposta = self.screen_manager.esperar_comando_usuario()

        if not resposta:
            return ComandoUsuario.VOLTAR

        return resposta

    def cadastrado_com_sucesso(self) -> None:
        self.screen_manager.feedback_sucesso("Cadastro realizado com sucesso!")

    def erro_cadastro(self, mensagem: str) -> None:
        self.screen_manager.feedback_erro(mensagem)
