from controller.abstract_controller import Controller
from controller.enumerators import ComandoUsuario
from model.enumerators import TipoProprietario
from model.proprietario import Proprietario
from view.proprietario import ProprietarioView
from daos.proprietario_dao import ProprietarioDAO


class ProprietarioController(Controller):
    def __init__(self, base_controller) -> None:
        # self.__proprietarios = []
        self.__proprietarios = ProprietarioDAO()
        self.__base_controller = base_controller
        self.__proprietario_view = ProprietarioView(
            self.__base_controller.screen_manager
        )

    @property
    def proprietarios(self):
        return self.__proprietarios

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
            # self.__proprietarios.append(novo_proprietario)
            self.__proprietarios.add(novo_proprietario)

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
            case ComandoUsuario.DESLOGAR:
                self.__base_controller.usuario_logado = None
                self.__base_controller.inicio_deslogado()
            case ComandoUsuario.VER_PERFIL_PROPRIETARIO:
                self.__mostrar_perfil()

            case ComandoUsuario.VER_IMOVEIS_PROPRIETARIO:
                self.__mostrar_imoveis_proprietario()

            case ComandoUsuario.CADASTRAR_NOVO_IMOVEL:
                self.__cadastrar_novo_imovel()

            case ComandoUsuario.VISUALIZAR_RELATORIO_ALUGUEIS:
                self.__visualizar_relatorio_aluguel()

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
            "documento": usuario_logado.documento,
        }

    def __editar_perfil(self):
        dados_para_editar = self.__proprietario_view.editar_perfil(
            self.__get_proprietario_data()
        )

        email_do_usuario_logado = self.__base_controller.usuario_logado.email
        novo_usuario_logado = None

        for proprietario in self.__proprietarios:
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
        imoveis_para_exibir = []
        imoveis = self.__base_controller.usuario_logado.imoveis

        for imovel in imoveis:
            imoveis_para_exibir.append(
                {
                    "id": imovel.identificador,
                    "titulo": imovel.titulo,
                    "preco": imovel.preco,
                }
            )

        resposta = self.__proprietario_view.mostrar_imoveis_proprietario(
            imoveis_para_exibir
        )

        if resposta == ComandoUsuario.VOLTAR:
            self.__base_controller.iniciar()

        else:
            self.__mostrar_imovel(imoveis[resposta])

    def __mostrar_imovel(self, imovel):
        comando = self.__proprietario_view.mostrar_detalhes_imovel(
            self.__get_imovel_data(imovel)
        )

        match comando:
            case ComandoUsuario.VOLTAR:
                self.__mostrar_imoveis_proprietario()
            case ComandoUsuario.EDITAR_IMOVEL:
                self.__editar_imovel(imovel)
            case ComandoUsuario.EXCLUIR_IMOVEL:
                self.__excluir_imovel(imovel.identificador)

    def __editar_imovel(self, imovel):
        comando = self.__proprietario_view.editar_imovel(
            self.__get_imovel_data(imovel)
        )

        if comando == ComandoUsuario.VOLTAR:
            self.__mostrar_imovel(imovel)

        imovel.titulo = comando["titulo"]
        imovel.informacoes = comando["informacoes"]
        imovel.preco = float(comando["preco"])
        imovel.endereco = comando["endereco"]

        self.__proprietario_view.cadastrado_com_sucesso()

        self.__mostrar_imovel(imovel)

    def __get_imovel_data(self, imovel):
        return {
            "titulo": imovel.titulo,
            "informacoes": imovel.informacoes,
            "preco": imovel.preco,
            "endereco": imovel.endereco,
            "status": imovel.status.value,
        }

    def __excluir_imovel(self, imovel_id):
        self.__base_controller.usuario_logado.remover_imovel(imovel_id)
        self.__proprietario_view.excluido_com_sucesso()
        self.__mostrar_imoveis_proprietario()

    def __cadastrar_novo_imovel(self):
        try:
            novo_imovel = self.__base_controller.imovel.cadastrar_imovel()
            if not novo_imovel:
                raise Exception()
            self.__base_controller.usuario_logado.adicionar_imovel(novo_imovel)
            self.__proprietario_view.cadastrado_com_sucesso()
            self.__mostrar_imoveis_proprietario()

        except Exception:
            self.__proprietario_view.erro_cadastro(
                "Erro ao cadastrar! Tente de novo."
            )
            self.__cadastrar_novo_imovel()

    def __visualizar_relatorio_aluguel(self):
        data = {}
        imoveis = self.__base_controller.usuario_logado.imoveis

        for imovel in imoveis:
            data[imovel.identificador] = {
                "titulo": imovel.titulo,
                "preco": imovel.preco,
                "alugueis": [],
            }

            for aluguel in imovel.historico_aluguel:
                data[imovel.identificador]["alugueis"].append(
                    {
                        "locatario": aluguel.locatario.nome,
                        "data_inicio": aluguel.data_locacao,
                        "diarias": aluguel.diarias,
                    }
                )
        self.__proprietario_view.visualizar_relatorio_alugueis(data)
        self.iniciar()
