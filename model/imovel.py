from hashlib import md5

from enumerators import StatusImovel
from locador import Locador

from utils.decorators import validar_tipo_do_parametro


class Imovel:
    def __init__(
        self,
        endereco: str,
        preco: float,
        informacoes: str,
        proprietario: Locador,
    ) -> None:
        self.__endereco = None
        self.__preco = None
        self.__informacoes = None
        self.__proprietario: Locador = None
        self.__status: StatusImovel = StatusImovel.DISPONIVEL
        self.__identificador: str = None

        self.__validar_parametros_construtor(
            endereco, preco, informacoes, proprietario
        )

    def __validar_parametros_construtor(
        self,
        endereco: str,
        preco: float,
        informacoes: str,
        proprietario: Locador,
    ) -> None:
        self.endereco = endereco
        self.preco = preco
        self.informacoes = informacoes

        if proprietario is not None and isinstance(proprietario, Locador):
            self.__proprietario = proprietario

        chave_id = f"{endereco}{preco}{informacoes}{proprietario.nome}"
        self.__identificador = md5(chave_id.encode("utf-8")).hexdigest()

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    @validar_tipo_do_parametro(str)
    def endereco(self, endereco: str) -> None:
        self.__endereco = endereco

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    @validar_tipo_do_parametro(float)
    def preco(self, preco: float) -> None:
        self.__preco = preco

    @property
    def informacoes(self) -> str:
        return self.__informacoes

    @informacoes.setter
    @validar_tipo_do_parametro(str)
    def informacoes(self, informacoes: str) -> None:
        self.__informacoes = informacoes

    @property
    def identificador(self) -> str:
        return self.__identificador

    @property
    def proprietario(self) -> Locador:
        return self.__proprietario

    @property
    def status(self) -> StatusImovel:
        return self.__status

    @status.setter
    @validar_tipo_do_parametro(StatusImovel)
    def status(self, status: StatusImovel) -> None:
        self.__status = status
