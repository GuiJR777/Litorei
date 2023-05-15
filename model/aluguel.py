from datetime import datetime
from model.imovel import Imovel


class Aluguel:
    def __init__(self, locatario: str, imovel: str) -> None:
        self.__locatario = None
        self.__imovel: Imovel = None
        self.__data_locacao = None
        self.__data_devolucao = None

        self.__validar_parametros_construtor(locatario, imovel)

    def __validar_parametros_construtor(
        self, locatario: str, imovel: str
    ) -> None:
        self.__locatario = locatario

        self.__imovel = imovel

    @property
    def locatario(self):
        return self.__locatario

    @property
    def imovel(self) -> Imovel:
        return self.__imovel

    @property
    def data_locacao(self) -> str:
        return self.__data_locacao

    def registrar_locacao(self) -> None:
        self.__data_locacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @property
    def data_devolucao(self) -> str:
        return self.__data_devolucao

    def registrar_devolucao(self) -> None:
        self.__data_devolucao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
