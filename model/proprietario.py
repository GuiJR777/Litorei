from typing import List
import pickle

from model.enumerators import TipoProprietario
from model.exceptions import (
    ImovelNaoEncontradoException,
    ImovelJaCadastradoException,
)
from model.imovel import Imovel
from model.usuario import Usuario
from utils.decorators import validar_tipo_do_parametro
from daos.imovel_dao import ImovelDAO


class Proprietario(Usuario):
    def __init__(
        self,
        nome: str,
        email: str,
        telefone: str,
        senha: str,
        documento: str,
        tipo: TipoProprietario,
    ) -> None:
        super().__init__(nome, email, telefone, senha, documento)
        # self.__imoveis: List[Imovel] = []
        self.__imoveis = ImovelDAO()
        self.__tipo: TipoProprietario = None

        self.tipo = tipo

    @property
    def tipo(self) -> TipoProprietario:
        return self.__tipo

    @property
    def imoveis(self):
        return self.__imoveis

    @tipo.setter
    @validar_tipo_do_parametro(TipoProprietario)
    def tipo(self, tipo: TipoProprietario) -> None:
        self.__tipo = tipo

    def adicionar_imovel(self, imovel_para_adicionar: Imovel) -> None:
        imoveis = self.__imoveis.get_all()
        for imovel in imoveis:
            if imovel.identificador == imovel_para_adicionar.identificador:
                raise ImovelJaCadastradoException(imovel_para_adicionar.identificador)
        
        imovel_para_adicionar.proprietario = self
        self.__imoveis.add(imovel_para_adicionar)

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
