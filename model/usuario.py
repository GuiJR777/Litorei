from decorators import validar_tipo_do_parametro


class Usuario:
    def __init__(
        self, nome: str, email: str, telefone: str, senha: str, documento: str
    ) -> None:
        self.__nome = None
        self.__email = None
        self.__telefone = None
        self.__senha = None

        self.__validar_parametros_construtor(
            nome, email, telefone, senha, documento
        )

    def __validar_parametros_construtor(
        self, nome: str, email: str, telefone: str, senha: str, documento: str
    ) -> None:
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.documento = documento

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    @validar_tipo_do_parametro(str)
    def nome(self, nome) -> None:
        self.__nome = nome

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    @validar_tipo_do_parametro(str)
    def email(self, email) -> None:
        self.__email = email

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    @validar_tipo_do_parametro(str)
    def telefone(self, telefone) -> None:
        self.__telefone = telefone

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    @validar_tipo_do_parametro(str)
    def senha(self, senha) -> None:
        self.__senha = senha

    @property
    def documento(self) -> str:
        return self.__documento

    @documento.setter
    @validar_tipo_do_parametro(str)
    def documento(self, documento) -> None:
        self.__documento = documento
