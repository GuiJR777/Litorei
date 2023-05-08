from controller.base_controller import BaseController
from screens.terminal.welcome import Welcome


if __name__ == "__main__":
    base_controller = BaseController()
    base_controller.iniciar()
    tela_inicial = Welcome(base_controller.view())
    tela_inicial.show_welcome()
    tela_inicial.entrada()
