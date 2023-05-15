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

    def iniciar(self, name):
        self.screen_manager.trocar_de_tela(
            Telas.INICIO_PROPRIETARIO, name=name)
        resposta = self.screen_manager.esperar_comando_usuario()

        match resposta:
            case "1":
                return ComandoUsuario.VER_PERFIL_PROPRIETARIO
            case "2":
                return ComandoUsuario.VER_IMOVEIS_PROPRIETARIO
            case "3":
                return ComandoUsuario.CADASTRAR_NOVO_IMOVEL
            case "4":
                return ComandoUsuario.SAIR

    def mostrar_perfil(self, data):
        self.screen_manager.trocar_de_tela(
            Telas.PERFIL_PROPRIETARIO, data=data)
        resposta = self.screen_manager.esperar_comando_usuario()

        match resposta:
            case "1":
                return ComandoUsuario.EDITAR_PERFIL_PROPRIETARIO
            case "2":
                return ComandoUsuario.VOLTAR

    def editar_perfil(self, data):
        self.screen_manager.trocar_de_tela(
            Telas.EDITAR_PERFIL_PROPRIETARIO, data=data)
        return self.screen_manager.esperar_comando_usuario()
    
    def mostrar_imoveis_proprietario(self):
        self.screen_manager.trocar_de_tela(Telas.MOSTRAR_IMOVEIS_PROPRIETARIO)

    def cadastrar_novo_imovel(self):
        self.screen_manager.trocar_de_tela(Telas.CADASTRO_IMOVEL)    