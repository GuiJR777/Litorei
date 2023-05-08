from view.abstract_view import View
from view.imovel import ImovelView
from view.locatario import LocatarioView
from view.proprietario import ProprietarioView


class BaseView(View):
    def __init__(self) -> None:
        self.__locatario = None
        self.__proprietario = None
        self.__imovel = None

    def iniciar(self) -> None:
        self.__locatario = LocatarioView()
        self.__proprietario = ProprietarioView()
        self.__imovel = ImovelView()

    @property
    def locatario(self) -> LocatarioView:
        return self.__locatario

    @property
    def proprietario(self) -> ProprietarioView:
        return self.__proprietario

    @property
    def imovel(self) -> ImovelView:
        return self.__imovel
