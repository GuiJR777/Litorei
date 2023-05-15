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
                self.__mostrar_perfil()

            case ComandoUsuario.VER_IMOVEIS_PROPRIETARIO:
                self.__mostrar_imoveis_proprietario()

            case ComandoUsuario.CADASTRAR_NOVO_IMOVEL:
                self.__cadastrar_novo_imovel()

    def __mostrar_perfil(self):
        comando = self.__proprietario_view.mostrar_perfil(
            self.__get_proprietario_data()
        )

        match comando:
            case ComandoUsuario.VOLTAR:
                self.iniciar()
            case ComandoUsuario.EDITAR_PERFIL_PROPRIETARIO:
                self.__editar_perfil()

    def __get_proprietario_data(self):
        usuario_logado = self.__base_controller.usuario_logado

        return {
            "nome": usuario_logado.nome,
            "email": usuario_logado.email,
            "telefone": usuario_logado.telefone,
            "documento": usuario_logado.documento
        }

    def __editar_perfil(self):
        dados_para_editar = self.__proprietario_view.editar_perfil(
            self.__get_proprietario_data()
        )

        email_do_usuario_logado = self.__base_controller.usuario_logado.email
        novo_usuario_logado = None

        for proprietario in self.__proprietario:
            if proprietario.email == email_do_usuario_logado:
                proprietario.nome = dados_para_editar["nome"]
                proprietario.email = dados_para_editar["email"]
                proprietario.telefone = dados_para_editar["telefone"]
                proprietario.documento = dados_para_editar["documento"]
                novo_usuario_logado = proprietario
                break

        if novo_usuario_logado:
            self.__base_controller.usuario_logado = novo_usuario_logado
            self.__proprietario_view.cadastrado_com_sucesso()
            self.__mostrar_perfil()

    def __mostrar_imoveis_proprietario(self):
        self.__proprietario_view.mostrar_imoveis_proprietario() 

    def __cadastrar_novo_imovel(self):
        novo_imovel = self.__base_controller.imovel.cadastrar_imovel()    
        if not novo_imovel:
                raise Exception()
        #novo_proprietario.adicionar_imovel(novo_imovel)