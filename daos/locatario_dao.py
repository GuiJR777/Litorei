from daos.dao import DAO
from model.locatario import Locatario

class LocatarioDAO(DAO):
    def __init__(self):
        super().__init__('locatario.pkl')
    
    def add(self, locatario: Locatario):
        if (isinstance(locatario, Locatario)) and (locatario is not None) and isinstance(locatario.documento, str):
            super().add(locatario.documento,locatario)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

    def update(self, locatario: Locatario):
        if locatario is not None and isinstance(locatario, Locatario):
            super().update(locatario)    
