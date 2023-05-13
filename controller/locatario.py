from controller.abstract_controller import Controller
from controller.enumerators import ComandoUsuario
from view.locatario import LocatarioView
from model.locatario import Locatario




class LocatarioController(Controller):
    def __init__(self, base_controller) -> None:
        self.__locatario = []  
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
            self.__locatario.append(novo_locatario)
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
                self.__mostrar_perfil()
            case ComandoUsuario.VER_CONTRATOS_LOCATARIO:
                print("Ver contratos locatário")
                input("Pressione enter para continuar...")
                self.iniciar()

    def __mostrar_perfil(self):
        comando = self.__locatario_view.mostrar_perfil(
            self.__get_locatario_data()
        )

        match comando:
            case ComandoUsuario.VOLTAR:
                self.iniciar()
            case ComandoUsuario.EDITAR_PERFIL_LOCATARIO:
                self.__editar_perfil()     

    def __get_locatario_data(self):
        usuario_logado = self.__base_controller.usuario_logado

        return {
            "nome": usuario_logado.nome,
            "email": usuario_logado.email,
            "telefone": usuario_logado.telefone,
            "documento": usuario_logado.documento
        }

    def __editar_perfil(self):
        dados_para_editar = self.__locatario_view.editar_perfil(
            self.__get_locatario_data()
        )

        email_do_usuario_logado = self.__base_controller.usuario_logado.email
        novo_usuario_logado = None

        for locatario in self.__locatario:
            if locatario.email == email_do_usuario_logado:
                locatario.nome = dados_para_editar["nome"]
                locatario.email = dados_para_editar["email"]
                locatario.telefone = dados_para_editar["telefone"]
                locatario.documento = dados_para_editar["documento"]
                novo_usuario_logado = locatario
                break

        if novo_usuario_logado:
            self.__base_controller.usuario_logado = novo_usuario_logado
            self.__locatario_view.cadastrado_com_sucesso()
            self.__mostrar_perfil()              
