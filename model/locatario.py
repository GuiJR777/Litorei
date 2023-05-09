from model.aluguel import Aluguel
from model.imovel import Imovel
from model.usuario import Usuario
from model.enumerators import StatusImovel
from model.exceptions import (
    JaPossuiAluguelException,
    ImovelIndisponivelException,
    NaoPossuiImovelAlugadoException,
)


class Locatario(Usuario):
    def __init__(
        self, nome: str, email: str, telefone: str, senha: str, documento: str
    ) -> None:
        super().__init__(nome, email, telefone, senha, documento)
        self.__aluguel: Aluguel = None

    @property
    def aluguel(self) -> Aluguel:
        return self.__aluguel

    def alugar_imovel(self, imovel: Imovel) -> None:
        if self.aluguel:
            raise JaPossuiAluguelException()

        if not imovel or not isinstance(imovel, Imovel):
            raise TypeError("Imóvel inválido")

        if imovel.status != StatusImovel.DISPONIVEL:
            raise ImovelIndisponivelException()

        imovel.status = StatusImovel.ALUGADO
        aluguel = Aluguel(self, imovel)

        self.__aluguel = aluguel

    def devolver_imovel(self) -> None:
        if not self.aluguel:
            raise NaoPossuiImovelAlugadoException()

        self.aluguel.imovel.status = StatusImovel.DISPONIVEL
        self.__aluguel = None
