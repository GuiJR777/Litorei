import enum


class TiposDeRespostas(enum.Enum):
    TEXTO = "texto"
    NUMERICO = "numerico"
    EMAIL = "email"
    SENHA = "senha"
    SIM_OU_NAO = "sim_ou_nao"
    MULTIPLA_ESCOLHA = "multipla_escolha"


class Telas(enum.Enum):
    WELCOME = "welcome"
    INICIO_DESLOGADO = "inicio_deslogado"
    AGRADECIMENTO = "agradecimento"
    CADASTRO_LOGIN = "cadastro_login"
    LOGIN = "login"
    CADASTRO_USUARIO = "cadastro_usuario"
    CADASTRO_LOCATARIO = "cadastro_locatario"
