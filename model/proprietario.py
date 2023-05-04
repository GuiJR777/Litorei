from typing import List

from enumerators import TipoProprietario
from exceptions import ImovelNaoEncontradoException
from imovel import Imovel
from usuario import Usuario

from utils.decorators import validar_tipo_do_parametro


class Proprietario(Usuario):
    def __init__(
        self,
        nome: str,
        email: str,
        telefone: str,
        senha: str,
        documento: str,
        tipo: TipoProprietario,
        titulo: str,
        endereco: str,
        preco: str,
        informacoes: str,
    ) -> None:
        super().__init__(nome, email, telefone, senha, documento)
        self.__imoveis: List[Imovel] = []
        self.__tipo: TipoProprietario = None

        self.tipo = tipo
        self.criar_imovel(titulo, endereco, preco, informacoes)

    @property
    def tipo(self) -> TipoProprietario:
        return self.__tipo

    @property
    def imoveis(self) -> List[Imovel]:
        return self.__imoveis

    @tipo.setter
    @validar_tipo_do_parametro(TipoProprietario)
    def tipo(self, tipo: TipoProprietario) -> None:
        self.__tipo = tipo

    @validar_tipo_do_parametro(str)
    def criar_imovel(self, titulo, endereco, preco, informacoes) -> None:
        imovel = Imovel(titulo, endereco, preco, informacoes, self)

        self.__imoveis.append(imovel)

    @validar_tipo_do_parametro(str)
    def buscar_imovel(self, identificador: str) -> Imovel:
        for imovel in self.__imoveis:
            if imovel.identificador == identificador:
                return imovel
        raise ImovelNaoEncontradoException(identificador)

    @validar_tipo_do_parametro(str)
    def remover_imovel(self, identificador: str) -> None:
        imovel = self.buscar_imovel(identificador)

        if imovel:
            self.__imoveis.remove(imovel)
