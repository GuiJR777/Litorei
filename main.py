import argparse

import flet as ft

from controller.base_controller import BaseController
from screens.graphic.screen_manager import GUIScreenManager
from screens.terminal.screen_manager import TerminalScreenManager


def modo_grafico(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 1920
    page.window_height = 1080
    page.window_center()

    screen_manager = GUIScreenManager(page)
    BaseController(screen_manager).iniciar()


def modo_terminal() -> None:
    screen_manager = TerminalScreenManager()
    BaseController(screen_manager).iniciar()


def get_running_mode() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--modo", choices=["grafico", "terminal"], default="grafico"
    )
    args = parser.parse_args()
    return args.modo


if __name__ == "__main__":
    modo_de_execucao = get_running_mode()

    match modo_de_execucao:
        case "terminal":
            modo_terminal()
        case "grafico":
            ft.app(target=modo_grafico)
