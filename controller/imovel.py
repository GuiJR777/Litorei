from controller.abstract_controller import Controller
from controller.enumerators import ComandoUsuario
from model.enumerators import StatusImovel
from model.imovel import Imovel

from view.imovel import ImovelView


class ImovelController(Controller):
    def __init__(self, base_controller) -> None:
        self.__imoveis = []
        self.__base_controller = base_controller
        self.__imovel_view = ImovelView(self.__base_controller.screen_manager)

    def listar_imoveis(self):
        imoveis_data = []

        if len(self.__imoveis) == 0:
            self.__imovel_view.erro_listar_imoveis()
            self.__base_controller.iniciar()

        for imovel in self.__imoveis:
            if imovel.status != StatusImovel.DISPONIVEL:
                continue

            imoveis_data.append(
                {
                    "id": imovel.identificador,
                    "titulo": imovel.titulo,
                    "preco": imovel.preco,
                }
            )
        resposta = self.__imovel_view.listar_imoveis(imoveis_data)

        if resposta == ComandoUsuario.VOLTAR:
            self.__base_controller.iniciar()

        else:
            self.__mostrar_imovel(self.__imoveis[resposta].identificador)

    def __mostrar_imovel(self, imovel_id) -> None:
        imovel = self.__buscar_imovel(imovel_id)

        imovel_data = {
            "titulo": imovel.titulo,
            "informacoes": imovel.informacoes,
            "preco": imovel.preco,
            "endereco": imovel.endereco,
        }

        comando = self.__imovel_view.mostrar_imovel(imovel_data)

        match comando:
            case ComandoUsuario.ALUGAR_IMOVEL:
                if not self.__base_controller.usuario_logado:
                    self.__base_controller.tela_de_cadastro_login()

                self.__base_controller.locatario.alugar_imovel(imovel)
            case ComandoUsuario.VOLTAR:
                self.listar_imoveis()

    def __buscar_imovel(self, imovel_id) -> None:
        for imovel in self.__imoveis:
            if imovel.identificador == imovel_id:
                return imovel

    def cadastrar_imovel(self):
        dados_imovel = self.__imovel_view.cadastrar()

        if dados_imovel == ComandoUsuario.VOLTAR:
            return None

        try:
            dados_imovel["preco"] = float(dados_imovel["preco"])
            novo_imovel = Imovel(**dados_imovel)
            self.__imoveis.append(novo_imovel)
            return novo_imovel

        except Exception:
            return None
