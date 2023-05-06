from screens.terminal.screen import Screen


class ListagemImoveis(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.titulo = "Imóveis"

    def entrada(self) -> None:
        self.show_titulo()
        self.__show_options()

    def __show_options(self) -> None:
        imoveis = self.__get_imoveis()

        for index, imovel in enumerate(imoveis):
            self.add_opcao(index + 1, (self.__show_imovel, imovel))
            self.show_opcao(index + 1, imovel)

        self.add_opcao(len(imoveis) + 1, self.voltar_para_tela_anterior)
        self.show_opcao(len(imoveis) + 1, "Voltar")

        self.get_opcao()

    def get_opcao(self) -> None:
        opcao = input("Opção: ")

        if not self.opcao_valida(opcao):
            self.show_error("Opção inválida!")
            self.clear_terminal(1)
            self.entrada()

        self.clear_terminal(1)
        metodo = self.mapa_opcoes[int(opcao)][0]
        argumento = self.mapa_opcoes[int(opcao)][1]
        metodo(argumento)

    def __get_imoveis(self) -> None:
        return [
            "Lindo apartamento em Copacabana, com vista para o mar. - R$ 350,00.", # noqa
            "Casa espaçosa em São Paulo, ideal para famílias. - R$ 500,00.",
            "Chalé aconchegante em Campos do Jordão, perfeito para um final de semana romântico. - R$ 300,00.", # noqa
            "Cobertura luxuosa em Brasília, com piscina e churrasqueira. - R$ 1.200,00.", # noqa
            "Sítio tranquilo em Minas Gerais, cercado por natureza. - R$ 400,00.", # noqa
        ]

    def __show_imovel(self, imovel: str) -> None:
        self.clear_terminal()
        self.show(imovel)
        input("Pressione enter para voltar...")
        self.clear_terminal(1)
        self.entrada()
