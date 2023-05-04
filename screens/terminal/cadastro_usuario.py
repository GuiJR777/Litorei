from screens.terminal.screen import Screen
from screens.terminal.enumerators import TiposDeRespostas
from model.enumerators import TipoLocador


class CadastroUsuario(Screen):
    def __init__(self) -> None:
        super().__init__()
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

    def __iniciar_cadastro_locatario(self) -> None:
        pass

    def __questoes_comuns(self) -> None:
        data = {
            "nome": self.questionar(
                "Qual o seu nome?", TiposDeRespostas.TEXTO
            ),
            "email": self.questionar(
                "Qual o seu email?", TiposDeRespostas.EMAIL
            ),
            "telefone": self.questionar(
                "Qual o seu telefone?", TiposDeRespostas.TEXTO
            ),
            "senha": self.questionar(
                "Crie uma senha:", TiposDeRespostas.TEXTO
            ),
        }

        self.__payload.update(data)

    def __questionar_pf_ou_pj(self) -> None:
        resposta = self.questionar(
            "Você é pessoa física?", TiposDeRespostas.SIM_NAO
        )

        if resposta == "s":
            self.__payload.update({"tipo": TipoLocador.PESSOA_FISICA})
            self.__questionar_cpf()

        elif resposta == "n":
            self.__payload.update({"tipo": TipoLocador.PESSOA_JURIDICA})
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
                    "Qual o seu CPF?", TiposDeRespostas.TEXTO
                )
            }
        )

    def __criar_primeiro_imovel(self) -> None:
        self.digitar_na_tela("Agora vamos cadastrar o seu primeiro imóvel")
