from datetime import datetime
from model.imovel import Imovel
from utils.decorators import validar_tipo_do_parametro


class Aluguel:
    def __init__(self, locatario: str, imovel: str) -> None:
        self.__locatario = None
        self.__imovel: Imovel = None
        self.__data_locacao = None
        self.__data_devolucao = None
        self.__diarias = None

        self.__validar_parametros_construtor(locatario, imovel)

    def __validar_parametros_construtor(
        self, locatario: str, imovel: str
    ) -> None:
        self.__locatario = locatario
        self.__imovel = imovel
        self.__imovel.adicionar_ao_historico(self)

    @property
    def locatario(self):
        return self.__locatario

    @property
    def imovel(self) -> Imovel:
        return self.__imovel

    @property
    def data_locacao(self) -> str:
        return self.__data_locacao

    @property
    def diarias(self) -> int:
        return self.__diarias

    @diarias.setter
    @validar_tipo_do_parametro(int)
    def diarias(self, diarias) -> None:
        self.__diarias = diarias

    def registrar_locacao(self) -> None:
        self.__data_locacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @property
    def data_devolucao(self) -> str:
        return self.__data_devolucao

    def registrar_devolucao(self) -> None:
        self.__data_devolucao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
