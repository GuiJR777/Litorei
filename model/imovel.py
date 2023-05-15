from hashlib import md5

from model.enumerators import StatusImovel

from utils.decorators import validar_tipo_do_parametro


class Imovel:
    def __init__(
        self,
        titulo: str,
        endereco: str,
        preco: float,
        informacoes: str,
    ) -> None:
        self.__titulo = titulo
        self.__endereco = None
        self.__preco = None
        self.__informacoes = None
        self.__proprietario = None
        self.__status: StatusImovel = StatusImovel.DISPONIVEL
        self.__identificador: str = None
        self.__historico_aluguel = []

        self.__validar_parametros_construtor(
            titulo, endereco, preco, informacoes
        )

    def __validar_parametros_construtor(
        self,
        titulo: str,
        endereco: str,
        preco: float,
        informacoes: str,
    ) -> None:
        self.titulo = titulo
        self.endereco = endereco
        self.preco = preco
        self.informacoes = informacoes

        chave_id = f"{titulo}{endereco}{preco}{informacoes}"
        self.__identificador = md5(chave_id.encode("utf-8")).hexdigest()

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    @validar_tipo_do_parametro(str)
    def titulo(self, titulo: str) -> None:
        self.__titulo = titulo

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
    def proprietario(self):
        return self.__proprietario

    @proprietario.setter
    def proprietario(self, proprietario) -> None:
        from model.proprietario import Proprietario

        if not isinstance(proprietario, Proprietario):
            raise TypeError("Proprietário inválido")
        self.__proprietario = proprietario

    @property
    def identificador(self) -> str:
        return self.__identificador

    @property
    def status(self) -> StatusImovel:
        return self.__status

    @status.setter
    @validar_tipo_do_parametro(StatusImovel)
    def status(self, status: StatusImovel) -> None:
        self.__status = status

    @property
    def historico_aluguel(self) -> list:
        return self.__historico_aluguel

    def adicionar_ao_historico(self, aluguel):
        self.__historico_aluguel.append(aluguel)
