from controller.abstract_controller import Controller
from controller.enumerators import ComandoUsuario
from model.exceptions import (
    ImovelIndisponivelException,
    JaPossuiAluguelException,
    NaoPossuiImovelAlugadoException,
)
from view.locatario import LocatarioView
from model.locatario import Locatario


class LocatarioController(Controller):
    def __init__(self, base_controller) -> None:
        self.__locatarios = []
        self.__base_controller = base_controller
        self.__locatario_view = LocatarioView(
            self.__base_controller.screen_manager
        )

    @property
    def locatarios(self):
        return self.__locatarios

    def cadastrar(self) -> None:
        dados_locatario = self.__locatario_view.cadastrar()

        if dados_locatario == ComandoUsuario.VOLTAR:
            self.__base_controller.cadastrar_usuario()

        e_valido = self.__validar_cadastro(dados_locatario)

        if e_valido != "OK":
            self.__locatario_view.erro_cadastro(e_valido)
            self.cadastrar()
            return

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
            case ComandoUsuario.DESLOGAR:
                self.__base_controller.usuario_logado = None
                self.__base_controller.inicio_deslogado()
            case ComandoUsuario.LISTAR_IMOVEIS:
                self.__base_controller.imovel.listar_imoveis()

            case ComandoUsuario.VER_PERFIL_LOCATARIO:
                self.__mostrar_perfil()
            case ComandoUsuario.VER_CONTRATOS_LOCATARIO:
                self.__ver_contrato()

    def __validar_cadastro(self, dados_locatario) -> str:
        if "@" not in dados_locatario["email"]:
            return "Email inválido!"

        if dados_locatario["senha"] != dados_locatario["confirmar_senha"]:
            return "Senhas não conferem!"

        if dados_locatario["documento"] == "":
            return "CPF inválido!"

        if not dados_locatario["documento"].isnumeric():
            return "CPF inválido!"

        if len(dados_locatario["documento"]) != 11:
            return "CPF inválido!"

        if dados_locatario["telefone"] == "":
            return "Telefone inválido!"

        if not dados_locatario["telefone"].isnumeric():
            return "Telefone inválido!"

        if dados_locatario["nome"] == "":
            return "Nome inválido!"

        del dados_locatario["confirmar_senha"]
        return "OK"

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
            "documento": usuario_logado.documento,
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

    def alugar_imovel(self, imovel) -> None:
        try:
            diarias = self.__locatario_view.diarias()
            if diarias == ComandoUsuario.VOLTAR:
                self.iniciar()
            else:
                self.__base_controller.usuario_logado.alugar_imovel(imovel)
                if self.__base_controller.usuario_logado.aluguel:
                    self.__base_controller.usuario_logado.aluguel.diarias = (
                        int(diarias)
                    )  # noqa
                    self.__locatario_view.aluguel_realizado_com_sucesso()
                    self.iniciar()
        except TypeError:
            self.__locatario_view.erro_alugar_imovel("Imóvel invalido!")
            self.iniciar()
        except JaPossuiAluguelException:
            self.__locatario_view.erro_alugar_imovel(
                "Você já possui um imóvel alugado!"
            )
            self.iniciar()
        except ImovelIndisponivelException:
            self.__locatario_view.erro_alugar_imovel(
                "Imóvel indisponível para aluguel!"
            )
            self.iniciar()

    def __ver_contrato(self):
        aluguel = self.__base_controller.usuario_logado.aluguel
        if not aluguel:
            self.__locatario_view.erro_ver_contrato()
            self.iniciar()

        aluguel_data = {
            "titulo": aluguel.imovel.titulo,
            "preco": aluguel.imovel.preco,
            "proprietario": aluguel.imovel.proprietario.nome,
            "endereco": aluguel.imovel.endereco,
            "checkin": aluguel.data_locacao,
            "diarias": aluguel.diarias,
        }

        comando = self.__locatario_view.ver_contrato(aluguel_data)

        match comando:
            case ComandoUsuario.DEVOLVER_IMOVEL:
                self.__devolver_imovel()
            case ComandoUsuario.VOLTAR:
                self.iniciar()

        self.iniciar()

    def __devolver_imovel(self):
        try:
            self.__base_controller.usuario_logado.devolver_imovel()
            self.__locatario_view.devolver_imovel_com_sucesso()
            self.iniciar()
        except NaoPossuiImovelAlugadoException:
            self.__locatario_view.erro_devolver_imovel()
            self.iniciar()
