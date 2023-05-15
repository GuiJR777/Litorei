from screens.terminal.abstract_screen import Screen
from screens.terminal.enumerators import TiposDeRespostas


class EditarImovel(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Tela de Edição de Imóvel"
        self.__imovel_data = None

    def entrada(self, imovel_data) -> None:
        self.__imovel_data = imovel_data
        self.clear_terminal()
        self.show_titulo()

    def campos(self) -> None:
        new_imovel_data = {}

        for campo, valor_atual in self.__imovel_data.items():
            nome_campo = campo.capitalize()
            editar = self.questionar(
                f"O atual valor de {nome_campo} é {valor_atual}. Deseja editar?",
                TiposDeRespostas.SIM_OU_NAO,
            )

            if editar == "n":
                new_imovel_data[campo] = valor_atual
                continue

            tipo_de_resposta = TiposDeRespostas.TEXTO

            if nome_campo == "Preco":
                tipo_de_resposta = TiposDeRespostas.NUMERICO

            new_imovel_data[campo] = self.questionar(
                f"Qual é o novo valor de {nome_campo}?", tipo_de_resposta
            )

        return new_imovel_data
