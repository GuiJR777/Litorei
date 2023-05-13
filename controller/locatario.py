from controller.abstract_controller import Controller
from controller.enumerators import ComandoUsuario
from view.locatario import LocatarioView
from model.locatario import Locatario

from para_testes import locatarios  # TODO: Remover


class LocatarioController(Controller):
    def __init__(self, base_controller) -> None:
        # self.__locatarios = []  TODO: descomentar
        self.__locatarios = locatarios # TODO: Remover
        self.__base_controller = base_controller
        self.__locatario_view = LocatarioView(
            self.__base_controller.screen_manager
        )

    def cadastrar(self) -> None:
        dados_locatario = self.__locatario_view.cadastrar()

        if dados_locatario == ComandoUsuario.VOLTAR:
            self.__base_controller.cadastrar_usuario()

        try:
            novo_locatario = Locatario(**dados_locatario)
            self.__locatarios.append(novo_locatario)
            self.__locatario_view.cadastrado_com_sucesso()
            self.__base_controller.usuario_logado = novo_locatario
            self.iniciar()
        except Exception:
            self.__locatario_view.erro_cadastro(
                "Erro ao cadastrar! Tente de novo."
            )
            self.__base_controller.cadastrar_usuario()

    def iniciar(self) -> None:
        comando = self.__locatario_view.iniciar(
            self.__base_controller.usuario_logado.nome
        )

        match comando:
            case ComandoUsuario.SAIR:
                self.__base_controller.sair()
            case ComandoUsuario.LISTAR_IMOVEIS:
                self.__base_controller.imovel.listar_imoveis()

            case ComandoUsuario.VER_PERFIL_LOCATARIO:
                print("Ver perfil locatário")
                input("Pressione enter para continuar...")
                self.iniciar()
            case ComandoUsuario.VER_CONTRATOS_LOCATARIO:
                print("Ver contratos locatário")
                input("Pressione enter para continuar...")
                self.iniciar()
