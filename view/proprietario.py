from controller.enumerators import ComandoUsuario
from screens.enumerators import Telas
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

    def excluido_com_sucesso(self) -> None:
        self.screen_manager.feedback_sucesso("Imóvel excluído com sucesso!")

    def iniciar(self, name):
        self.screen_manager.trocar_de_tela(
            Telas.INICIO_PROPRIETARIO, data={"name": name}
        )
        resposta = self.screen_manager.esperar_comando_usuario()

        match resposta:
            case "1":
                return ComandoUsuario.VER_PERFIL_PROPRIETARIO
            case "2":
                return ComandoUsuario.VER_IMOVEIS_PROPRIETARIO
            case "3":
                return ComandoUsuario.CADASTRAR_NOVO_IMOVEL
            case "4":
                return ComandoUsuario.VISUALIZAR_RELATORIO_ALUGUEIS
            case "5":
                return ComandoUsuario.DESLOGAR

    def mostrar_perfil(self, data):
        self.screen_manager.trocar_de_tela(
            Telas.PERFIL_PROPRIETARIO, data=data
        )
        resposta = self.screen_manager.esperar_comando_usuario()

        match resposta:
            case "1":
                return ComandoUsuario.EDITAR_PERFIL_PROPRIETARIO
            case "2":
                return ComandoUsuario.VOLTAR

    def editar_perfil(self, data):
        self.screen_manager.trocar_de_tela(
            Telas.EDITAR_PERFIL_PROPRIETARIO, data=data
        )
        return self.screen_manager.esperar_comando_usuario()

    def mostrar_imoveis_proprietario(self, imoveis_data: list[dict]) -> None:
        self.screen_manager.trocar_de_tela(
            Telas.MOSTRAR_IMOVEIS_PROPRIETARIO,
            data={"imoveis": imoveis_data},
        )
        resposta = self.screen_manager.esperar_comando_usuario()

        if int(resposta) == len(imoveis_data) + 1:
            return ComandoUsuario.VOLTAR
        return int(resposta) - 1

    def cadastrar_novo_imovel(self):
        self.screen_manager.trocar_de_tela(Telas.CADASTRO_IMOVEL)

    def mostrar_detalhes_imovel(self, imovel_data: dict) -> None:
        self.screen_manager.trocar_de_tela(
            Telas.MOSTRAR_IMOVEL,
            data={"data": imovel_data},
            eh_locatario=False,
        )
        resposta = self.screen_manager.esperar_comando_usuario()

        match resposta:
            case "1":
                return ComandoUsuario.EDITAR_IMOVEL
            case "2":
                return ComandoUsuario.EXCLUIR_IMOVEL
            case "3":
                return ComandoUsuario.VOLTAR

    def editar_imovel(self, imovel_data: dict) -> None:
        self.screen_manager.trocar_de_tela(
            Telas.EDITAR_IMOVEL, data={"data": imovel_data}
        )
        resposta = self.screen_manager.esperar_comando_usuario()

        if not resposta:
            return ComandoUsuario.VOLTAR

        return resposta

    def visualizar_relatorio_alugueis(self, relatorio_data) -> None:
        self.screen_manager.trocar_de_tela(
            Telas.RELATORIO_ALUGUEIS, data=relatorio_data
        )
        self.screen_manager.esperar_comando_usuario()

        return ComandoUsuario.VOLTAR
