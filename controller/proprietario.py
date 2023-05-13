from controller.abstract_controller import Controller
from controller.enumerators import ComandoUsuario
from view.proprietario import ProprietarioView
from model.proprietario import Proprietario
from model.enumerators import TipoProprietario


class ProprietarioController(Controller):
    def __init__(self, base_controller) -> None:
        self.__proprietario = []
        self.__base_controller = base_controller
        self.__proprietario_view = ProprietarioView(
            self.__base_controller.screen_manager
        )

    def cadastrar(self) -> None:
        dados_proprietario = self.__proprietario_view.cadastrar()

        if dados_proprietario == ComandoUsuario.VOLTAR:
            self.__base_controller.cadastrar_usuario()

        try:
            if dados_proprietario["tipo"] == "pf":
                dados_proprietario["tipo"] = TipoProprietario.PESSOA_FISICA
            elif dados_proprietario["tipo"] == "pj":
                dados_proprietario["tipo"] = TipoProprietario.PESSOA_JURIDICA

            novo_proprietario = Proprietario(**dados_proprietario)
            self.__proprietario.append(novo_proprietario)

            novo_imovel = self.__base_controller.imovel.cadastrar_imovel()

            if not novo_imovel:
                raise Exception()
            novo_proprietario.adicionar_imovel(novo_imovel)

            self.__proprietario_view.cadastrado_com_sucesso()
            self.__base_controller.usuario_logado = novo_proprietario
            self.iniciar()
        except Exception:
            self.__proprietario_view.erro_cadastro(
                "Erro ao cadastrar! Tente de novo."
            )
            self.__base_controller.cadastrar_usuario()

    def iniciar(self):
        comando = self.__proprietario_view.iniciar(
            self.__base_controller.usuario_logado.nome
        )
        match comando:
            case ComandoUsuario.SAIR:
                self.__base_controller.sair()
            case ComandoUsuario.VER_PERFIL_PROPRIETARIO:
                print("Ver perfil proprietario")
                input("Pressione enter para continuar...")
                self.iniciar()

            case ComandoUsuario.VER_IMOVEIS_PROPRIETARIO:
                print("Ver imoveis proprietarios")
                input("Pressione enter para continuar...")
                self.iniciar()
            case ComandoUsuario.CADASTRAR_NOVO_IMOVEL:
                print("Cadastrar novo imovel")
                input("Pressione enter para continuar...")
                self.iniciar()
