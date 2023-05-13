import enum


class TiposDeRespostas(enum.Enum):
    TEXTO = "texto"
    NUMERICO = "numerico"
    EMAIL = "email"
    SENHA = "senha"
    SIM_OU_NAO = "sim_ou_nao"
    MULTIPLA_ESCOLHA = "multipla_escolha"


class Telas(enum.Enum):
    AGRADECIMENTO = "agradecimento"
    CADASTRO_LOCATARIO = "cadastro_locatario"
    CADASTRO_PROPRIETARIO = "cadastro_proprietario"
    CADASTRO_LOGIN = "cadastro_login"
    CADASTRO_USUARIO = "cadastro_usuario"
    LISTAGEM_IMOVEIS = "listagem_imoveis"
    LOGIN = "login"
    INICIO_DESLOGADO = "inicio_deslogado"
    INICIO_LOCATARIO = "inicio_locatario"
    WELCOME = "welcome"
    CADASTRO_IMOVEL = "cadastro_imovel"
    INICIO_PROPRIETARIO = "inicio_proprietario"
    PERFIL_PROPRIETARIO = "perfil_proprietario"
    EDITAR_PERFIL_PROPRIETARIO = "editar_perfil_proprietario"
    PERFIL_LOCATARIO = "perfil_locatario"
    EDITAR_PERFIL_LOCATARIO = "editar_perfil_locatario"
