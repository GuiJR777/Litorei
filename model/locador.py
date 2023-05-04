from typing import List
from decorators import validar_tipo_do_parametro
from exceptions import ImovelNaoEncontradoException
from usuario import Usuario
from imovel import Imovel
from enumerators import TipoLocador


class Locador(Usuario):
    def __init__(
        self,
        nome: str,
        email: str,
        telefone: str,
        senha: str,
        documento: str,
        tipo: TipoLocador,
        endereco: str,
        preco: str,
        informacoes: str,
    ) -> None:
        super().__init__(nome, email, telefone, senha, documento)
        self.__imoveis: List[Imovel] = []
        self.__tipo: TipoLocador = None

        self.tipo = tipo
        self.criar_imovel(endereco, preco, informacoes)

    @property
    def tipo(self) -> TipoLocador:
        return self.__tipo

    @property
    def imoveis(self) -> List[Imovel]:
        return self.__imoveis

    @tipo.setter
    @validar_tipo_do_parametro(TipoLocador)
    def tipo(self, tipo: TipoLocador) -> None:
        self.__tipo = tipo

    @validar_tipo_do_parametro(str)
    def criar_imovel(self, endereco, preco, informacoes) -> None:
        imovel = Imovel(endereco, preco, informacoes, self)

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
