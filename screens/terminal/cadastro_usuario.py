from model.enumerators import TipoProprietario
from screens.terminal.abstract_screen import Screen
from screens.terminal.enumerators import TiposDeRespostas


class CadastroUsuario(Screen):
    def __init__(self, view) -> None:
        super().__init__(view)
        self.titulo = "Tela de Cadastro"
        self.__payload = {}

        self.add_opcao(1, self.__iniciar_cadastro_proprietario)
        self.add_opcao(2, self.__iniciar_cadastro_locatario)
        self.add_opcao(3, self.voltar_para_tela_anterior)

    def entrada(self) -> None:
        self.show_titulo()
        self.__iniciar_cadastro()

    def __iniciar_cadastro(self) -> None:
        self.show("Responda as perguntas abaixo para realizar o cadastro:")
        self.digitar_na_tela(
            "Você é proprietário ou está procurando um imóvel?"
        )
        self.show_opcao(1, "Proprietário")
        self.show_opcao(2, "Procurando um imóvel")
        self.show_opcao(3, "Voltar")

        self.get_opcao()

    def __iniciar_cadastro_proprietario(self) -> None:
        self.__questoes_comuns()
        self.__questionar_pf_ou_pj()
        self.__criar_primeiro_imovel()
        self.__mostra_resultado()
        self.view.proprietario.cadastrar(self.__payload)

    def __iniciar_cadastro_locatario(self) -> None:
        self.__questoes_comuns()
        self.__questionar_cpf()
        self.__mostra_resultado()
        self.view.locatario.cadastrar(self.__payload)

    def __questoes_comuns(self) -> None:
        data = {
            "nome": self.questionar(
                "Qual o seu nome?", TiposDeRespostas.TEXTO
            ),
            "email": self.questionar(
                "Qual o seu email?", TiposDeRespostas.EMAIL
            ),
            "telefone": self.questionar(
                "Qual o seu telefone?", TiposDeRespostas.NUMERICO
            ),
            "senha": self.questionar(
                "Crie uma senha:", TiposDeRespostas.TEXTO
            ),
        }

        self.__payload.update(data)

    def __questionar_pf_ou_pj(self) -> None:
        resposta = self.questionar(
            "Você é pessoa física?", TiposDeRespostas.SIM_OU_NAO
        )

        if resposta == "s":
            self.__payload.update({"tipo": TipoProprietario.PESSOA_FISICA})
            self.__questionar_cpf()

        elif resposta == "n":
            self.__payload.update({"tipo": TipoProprietario.PESSOA_JURIDICA})
            self.__payload.update(
                {
                    "documento": self.questionar(
                        "Qual o seu CNPJ?", TiposDeRespostas.TEXTO
                    )
                }
            )

    def __questionar_cpf(self) -> None:
        self.__payload.update(
            {
                "documento": self.questionar(
                    "Qual o seu CPF?", TiposDeRespostas.NUMERICO
                )
            }
        )

    def __criar_primeiro_imovel(self) -> None:
        self.digitar_na_tela("Agora vamos cadastrar o seu primeiro imóvel")
        self.__payload.update(
            {
                "titulo": self.questionar(
                    "Qual o título para o anúncio do seu imóvel?",
                    TiposDeRespostas.TEXTO,
                ),
                "endereco": self.questionar(
                    "Qual o endereço do seu imóvel?", TiposDeRespostas.TEXTO
                ),
                "preco": self.questionar(
                    "Qual o preço do seu imóvel?", TiposDeRespostas.TEXTO
                ),
                "informacoes": self.questionar(
                    "Descreva seu imóvel:", TiposDeRespostas.TEXTO
                ),
            }
        )

    # TODO: Remover esse método e adicionar ligações com as views
    def __mostra_resultado(self) -> None:
        self.clear_terminal(1)
        self.show_titulo()
        self.show_success("Seu cadastro foi realizado com sucesso!")
        self.show_info("Abaixo estão os dados que você cadastrou:")

        for chave, valor in self.__payload.items():
            print("=" * 100)
            self.show(f"{chave}: {valor}")
            print("=" * 100)

        input("\n\nPressione enter para voltar...")
        self.clear_terminal(1)
        self.voltar_para_tela_anterior()
