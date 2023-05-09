from typing import List

from model.enumerators import TipoProprietario
from model.exceptions import (
    ImovelNaoEncontradoException,
    ImovelJaCadastradoException,
)
from model.imovel import Imovel
from model.usuario import Usuario
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
        imovel,
    ) -> None:
        super().__init__(nome, email, telefone, senha, documento)
        self.__imoveis: List[Imovel] = []
        self.__tipo: TipoProprietario = None

        self.tipo = tipo
        self.adicionar_imovel(imovel)

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
    def adicionar_imovel(self, imovel_para_adicionar: Imovel) -> None:
        for imovel in self.__imoveis:
            identificador = imovel_para_adicionar.identificador
            if imovel.identificador == identificador:
                raise ImovelJaCadastradoException(identificador)

        if imovel is not None and isinstance(imovel, Imovel):
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
