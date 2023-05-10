from controller.base_controller import BaseController
from screens.terminal.screens_manager import ScreenManager


if __name__ == "__main__":
    screen_manager = ScreenManager()

    BaseController(screen_manager).iniciar()
