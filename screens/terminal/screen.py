import os
import random
from abc import ABC, abstractmethod
from time import sleep

from screens.terminal.log_colors import ColorPrinter


class Screen(ABC):
    def __init__(self) -> None:
        self.titulo = ""
        self.ultima_tela: Screen = None
        self.__color_printer = ColorPrinter()
        self.__mapa_opcoes = {
            0: self.sair,
        }

    @property
    def mapa_opcoes(self) -> dict:
        return self.__mapa_opcoes

    def add_opcao(self, opcao: int, funcao) -> None:
        self.__mapa_opcoes[opcao] = funcao

    @abstractmethod
    def entrada(self) -> None:
        self.show_info(self.__titulo)

    def trocar_de_tela(self, tela) -> None:
        self.clear_terminal(1)
        tela.ultima_tela = self
        tela.entrada()

    def voltar_para_tela_anterior(self) -> None:
        self.clear_terminal(1)
        self.ultima_tela.entrada()

    @staticmethod
    def show(content: str) -> None:
        print(content)

    def show_titulo(self) -> None:
        self.__color_printer.print_blue(
            f"""
🅻 🅸 🆃 🅾 🆁 🅴 🅸
{'=' * 100}
{self.titulo}
{'=' * 100}
            """
        )

    def show_opcao(self, opcao: int, content: str) -> None:
        self.__color_printer.print_yellow(f"{opcao} - {content}")

    def show_error(self, content: str) -> None:
        self.__color_printer.print_red(content)

    def show_success(self, content: str) -> None:
        self.__color_printer.print_green(content)

    def show_info(self, content: str) -> None:
        self.__color_printer.print_blue(content)

    @staticmethod
    def clear_terminal(time_to_wait: int = 0) -> None:
        sleep(time_to_wait)
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def digitar_na_tela(text, min_delay=0.01, max_delay=0.1) -> None:
        for char in text:
            print(char, end="", flush=True)
            delay = random.uniform(min_delay, max_delay)
            sleep(delay)
        print()

    def opcao_valida(self, opcao: str) -> bool:
        if (
            not opcao.isnumeric()
            or int(opcao) not in self.__mapa_opcoes.keys()
        ):
            return False
        return True

    def sair(self) -> None:
        self.clear_terminal(1)
        self.digitar_na_tela("Até logo!")
        self.clear_terminal(2)
        exit(0)
