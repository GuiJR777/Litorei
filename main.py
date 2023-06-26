import argparse

import flet as ft

from controller.base_controller import BaseController
from screens.graphic.screen_manager import GUIScreenManager
from screens.terminal.screen_manager import TerminalScreenManager


def modo_grafico(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window_full_screen = True
    page.window_center()
    page.fonts = {
        "Roboto": "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,700;1,400&display=swap"
    }
    page.font_family = "Roboto"
    page.bgcolor = "#fffff5"

    screen_manager = GUIScreenManager(page)
    BaseController(screen_manager).iniciar()


def modo_terminal() -> None:
    screen_manager = TerminalScreenManager()
    BaseController(screen_manager).iniciar()


def get_running_mode() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--modo", choices=["grafico", "terminal"], default="terminal"
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
