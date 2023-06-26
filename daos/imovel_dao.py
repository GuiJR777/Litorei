from daos.dao import DAO
from model.imovel import Imovel


class ImovelDAO(DAO):
    def __init__(self):
        super().__init__("imovel.pkl")

    def add(self, imovel: Imovel):
        if (
            (isinstance(imovel, Imovel))
            and (imovel is not None)
            and isinstance(imovel.identificador, str)
        ):
            super().add(imovel.identificador, imovel)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
