from colorama import init, Fore, Style


class ColorPrinter:
    def __init__(self) -> None:
        init()  # inicializa a biblioteca colorama

    def print_red(self, text) -> None:
        print(Fore.RED + text + Style.RESET_ALL)

    def print_green(self, text) -> None:
        print(Fore.GREEN + text + Style.RESET_ALL)

    def print_yellow(self, text) -> None:
        print(Fore.YELLOW + text + Style.RESET_ALL)

    def print_blue(self, text) -> None:
        print(Fore.BLUE + text + Style.RESET_ALL)
