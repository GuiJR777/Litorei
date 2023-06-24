from controller.enumerators import ComandoUsuario
from screens.enumerators import Telas
from view.abstract_view import View


class LocatarioView(View):
    def __init__(self, screen_manager) -> None:
        self.screen_manager = screen_manager

    def cadastrar(self) -> dict:
        self.screen_manager.trocar_de_tela(Telas.CADASTRO_LOCATARIO)
        resposta = self.screen_manager.esperar_comando_usuario()

        if not resposta:
            return ComandoUsuario.VOLTAR

        return resposta

    def cadastrado_com_sucesso(self) -> None:
        self.screen_manager.feedback_sucesso("Cadastro realizado com sucesso!")

    def erro_cadastro(self, mensagem: str) -> None:
        self.screen_manager.feedback_erro(mensagem)

    def iniciar(self, name) -> None:
        self.screen_manager.trocar_de_tela(
            Telas.INICIO_LOCATARIO, data={"name": name}
        )
        resposta = self.screen_manager.esperar_comando_usuario()

        match resposta:
            case "1":
                return ComandoUsuario.LISTAR_IMOVEIS
            case "2":
                return ComandoUsuario.VER_PERFIL_LOCATARIO
            case "3":
                return ComandoUsuario.VER_CONTRATOS_LOCATARIO
            case "4":
                return ComandoUsuario.DESLOGAR

    def mostrar_perfil(self, data):
        self.screen_manager.trocar_de_tela(Telas.PERFIL_LOCATARIO, data=data)
        resposta = self.screen_manager.esperar_comando_usuario()

        match resposta:
            case "1":
                return ComandoUsuario.EDITAR_PERFIL_LOCATARIO
            case "2":
                return ComandoUsuario.VOLTAR

    def editar_perfil(self, data):
        self.screen_manager.trocar_de_tela(
            Telas.EDITAR_PERFIL_LOCATARIO, data=data
        )
        return self.screen_manager.esperar_comando_usuario()

    def aluguel_realizado_com_sucesso(self) -> None:
        self.screen_manager.feedback_sucesso("Aluguel realizado com sucesso!")

    def erro_alugar_imovel(self, mensagem: str) -> None:
        self.screen_manager.feedback_erro(mensagem)

    def erro_ver_contrato(self):
        self.screen_manager.feedback_erro("Nenhum contrato encontrado")

    def ver_contrato(self, contrato_data: dict) -> None:
        self.screen_manager.trocar_de_tela(
            Telas.VER_CONTRATO_ALUGUEL, contrato_data=contrato_data
        )
        comando = self.screen_manager.esperar_comando_usuario()

        match comando:
            case "1":
                return ComandoUsuario.DEVOLVER_IMOVEL
            case "2":
                return ComandoUsuario.VOLTAR

    def devolver_imovel_com_sucesso(self) -> None:
        self.screen_manager.feedback_sucesso(
            "Devolução realizada com sucesso!"
        )

    def erro_devolver_imovel(self) -> None:
        self.screen_manager.feedback_erro("Erro ao devolver imóvel!")

    def diarias(self):
        self.screen_manager.trocar_de_tela(Telas.DIARIAS)
        comando = self.screen_manager.esperar_comando_usuario()

        if comando == "0" or not comando:
            return ComandoUsuario.VOLTAR

        return comando
