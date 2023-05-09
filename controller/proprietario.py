from controller.abstract_controller import Controller


class ProprietarioController(Controller):
    def __init__(self, base_controller) -> None:
        self.__base_controller = base_controller

    def iniciar(self) -> None:
        pass

    def processo(self) -> None:
        pass
