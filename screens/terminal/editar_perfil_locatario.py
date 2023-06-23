from screens.terminal.abstract_screen import Screen
from screens.enumerators import TiposDeRespostas


class EditarPerfilLocatario(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Tela de Edição de Perfil"
        self.__data = None

    def entrada(self, data) -> None:
        self.__data = data
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> None:
        new_data = {}

        for campo, valor_atual in self.__data.items():
            nome_campo = campo.capitalize()
            editar = self.questionar(
                f"O atual valor de {nome_campo} é {valor_atual}. Deseja editar?",
                TiposDeRespostas.SIM_OU_NAO,
            )

            if editar == "n":
                new_data[campo] = valor_atual
                continue

            tipo_de_resposta = TiposDeRespostas.TEXTO

            if nome_campo == "Email":
                tipo_de_resposta = TiposDeRespostas.EMAIL
            elif nome_campo == "Telefone" or nome_campo == "Documento":
                tipo_de_resposta = TiposDeRespostas.NUMERICO

            new_data[campo] = self.questionar(
                f"Qual é o novo valor de {nome_campo}?", tipo_de_resposta
            )

        return new_data
