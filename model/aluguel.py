from imovel import Imovel
from locatario import Locatario


class Aluguel(Locatario, Imovel):
    def __init__(self, locatario: str, imovel: str) -> None:
        self.__locatario: Locatario = None
        self.__imovel: Imovel = None
        self.__data_locacao = None
        self.__data_devolucao = None

        self.__validar_parametros_construtor(locatario, imovel)

    def __validar_parametros_construtor(
        self, locatario: str, imovel: str
    ) -> None:
        if locatario is not None and isinstance(locatario, Locatario):
            self.__locatario = locatario

        if imovel is not None and isinstance(imovel, Imovel):
            self.__imovel = imovel

    @property
    def locatario(self) -> Locatario:
        return self.__locatario

    @property
    def imovel(self) -> Imovel:
        return self.__imovel

    @property
    def data_locacao(self) -> str:
        return self.__data_locacao

    @property
    def data_devolucao(self) -> str:
        return self.__data_devolucao
