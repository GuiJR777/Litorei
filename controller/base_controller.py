from controller.abstract_controller import Controller
from controller.imovel import ImovelController
from controller.locatario import LocatarioController
from controller.proprietario import ProprietarioController
from view.base_view import BaseView


class BaseController(Controller):
    def __init__(self) -> None:
        self.__imovel = None
        self.__locatario = None
        self.__proprietario = None
        self.__view = None

    def iniciar(self) -> None:
        self.__view = BaseView()
        self.__imovel = ImovelController()
        self.__locatario = LocatarioController()
        self.__proprietario = ProprietarioController()

    @property
    def view(self) -> BaseView:
        return self.__view
