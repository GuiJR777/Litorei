from daos.dao import DAO
from model.proprietario import Proprietario

class ProprietarioDAO(DAO):
    def __init__(self):
        super().__init__('proprietario.pkl')
    
    def add(self, proprietario: Proprietario):
        if (isinstance(proprietario, Proprietario)) and (proprietario is not None) and isinstance(proprietario.documento, str):
            super().add(proprietario.documento,proprietario)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
