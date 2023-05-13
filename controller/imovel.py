from controller.abstract_controller import Controller
from controller.enumerators import ComandoUsuario
from model.imovel import Imovel

from view.imovel import ImovelView
from para_testes import imoveis  # TODO: Remover


class ImovelController(Controller):
    def __init__(self, base_controller) -> None:
        # self.__imoveis = [] TODO: descomentar
        self.__imoveis = imoveis  # TODO: Remover
        self.__base_controller = base_controller
        self.__imovel_view = ImovelView(self.__base_controller.screen_manager)

    def listar_imoveis(self):
        imoveis_data = []

        for imovel in self.__imoveis:
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
            print(self.__imoveis[resposta].titulo)  # TODO: Remover
            input("Pressione enter para continuar...")  # TODO: Remover
            self.listar_imoveis()  # TODO: Remover

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
