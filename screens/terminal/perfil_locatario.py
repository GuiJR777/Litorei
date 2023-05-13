from screens.terminal.abstract_screen import Screen


class PerfilLocatario(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Seu perfil!"
        self.__data = None

    def entrada(self, data) -> None:
        self.clear_terminal()
        self.show_titulo()
        self.__data = data

    def campos(self) -> str:
        self.show_info(
            f"""
{'=' * 30}
Nome: {self.__data['nome']}
Email: {self.__data['email']}
Telefone: {self.__data["telefone"]}
Documento: {self.__data["documento"]}
            """
        )

        return self.selecionar(
            {
                "1": "Editar perfil",
                "2": "Voltar",
            }
        )