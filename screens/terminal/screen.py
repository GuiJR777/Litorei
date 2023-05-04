import os
from abc import ABC, abstractmethod
import random
from time import sleep

from screens.terminal.log_colors import ColorPrinter


class Screen(ABC):
    def __init__(self) -> None:
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
        pass

    @staticmethod
    def show(content: str) -> None:
        print(content)

    def show_opcao(self, opcao: int, content: str) -> None:
        self.__color_printer.print_yellow(f"{opcao} - {content}")

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
            and int(opcao) not in self.__mapa_opcoes.keys()
        ):
            return False
        return True

    def sair(self) -> None:
        self.clear_terminal(1)
        self.digitar_na_tela("Até logo!")
        self.clear_terminal(2)
        exit(0)
