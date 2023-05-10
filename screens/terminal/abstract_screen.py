import os
import random
from abc import ABC, abstractmethod
from time import sleep

from getpass4 import getpass

from screens.terminal.enumerators import TiposDeRespostas
from screens.terminal.exceptions import UsuarioQuerVoltarException
from screens.terminal.log_colors import ColorPrinter


class Screen(ABC):
    def __init__(self) -> None:
        self.titulo = ""
        self.ultima_tela: Screen = None
        self.__color_printer = ColorPrinter()

    @abstractmethod
    def entrada(self) -> None:
        self.show_info(self.__titulo)

    @abstractmethod
    def campos(self) -> None:
        pass

    def show_titulo(self) -> None:
        self.__color_printer.print_blue(
            f"""
🅻 🅸 🆃 🅾 🆁 🅴 🅸
{'=' * 60}
{self.titulo}
{'=' * 60}
            """
        )

    def show_opcao(self, opcao: int, content: str) -> None:
        self.__color_printer.print_yellow(f"{opcao} - {content}")

    def show_error(self, content: str) -> None:
        self.__color_printer.print_red(content)
        input("Pressione enter para continuar...")

    def show_success(self, content: str) -> None:
        self.__color_printer.print_green(content)
        input("Pressione enter para continuar...")

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

    def questionar(
        self,
        questao: str,
        tipo_resposta: TiposDeRespostas,
        opcoes_validas: list = [],
    ) -> str:
        self.digitar_na_tela(questao)

        if tipo_resposta == TiposDeRespostas.SIM_OU_NAO:
            resposta = input("Responda com 's' ou 'n': ")
        elif tipo_resposta == TiposDeRespostas.SENHA:
            resposta = getpass("Resposta: ")
        else:
            resposta = input("Resposta: ")

        try:
            match tipo_resposta:
                case TiposDeRespostas.NUMERICO:
                    if not resposta.isnumeric():
                        raise ValueError(
                            "Resposta inválida, precisa ser um número"
                        )
                case TiposDeRespostas.TEXTO:
                    if not resposta:
                        raise ValueError(
                            "Resposta inválida, precisa ser um texto"
                        )
                case TiposDeRespostas.SIM_OU_NAO:
                    if resposta.lower() not in ["s", "n"]:
                        raise ValueError(
                            "Resposta inválida, precisa ser 's' ou 'n'"
                        )
                case TiposDeRespostas.EMAIL:
                    if "@" not in resposta:
                        raise ValueError(
                            "Resposta inválida, precisa ser um email"
                        )
                case TiposDeRespostas.MULTIPLA_ESCOLHA:
                    if resposta not in opcoes_validas:
                        raise ValueError(
                            "Resposta inválida, precisa ser uma das opções:"
                            + ", ".join(opcoes_validas)
                        )
                case TiposDeRespostas.SENHA:
                    if not resposta:
                        raise ValueError(
                            "Resposta inválida, precisa ser uma senha"
                        )

        except ValueError as error:
            self.show_error(str(error))
            tentar_novamente = self.questionar(
                "Tentar novamente?",
                TiposDeRespostas.SIM_OU_NAO
                )
            if tentar_novamente == "n":
                raise UsuarioQuerVoltarException()
            return self.questionar(questao, tipo_resposta)

        return resposta

    def selecionar(self, opcoes: dict) -> None:
        for opcao, descricao in opcoes.items():
            self.show_opcao(opcao, descricao)

        opcao_selecionada = input("Opção: ")

        if opcao_selecionada not in opcoes.keys():
            self.show_error("Opção inválida!")
            self.clear_terminal(1)
            self.entrada()

        self.clear_terminal(1)

        return opcao_selecionada

    def sair(self) -> None:
        self.clear_terminal(1)
        self.digitar_na_tela("Até logo!")
        self.clear_terminal(2)
        exit(0)
