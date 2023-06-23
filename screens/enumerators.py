import enum


class TiposDeRespostas(enum.Enum):
    TEXTO = "texto"
    NUMERICO = "numerico"
    EMAIL = "email"
    SENHA = "senha"
    SIM_OU_NAO = "sim_ou_nao"
    MULTIPLA_ESCOLHA = "multipla_escolha"


class Telas(enum.Enum):
    AGRADECIMENTO = "/agradecimento"
    CADASTRO_LOCATARIO = "/locatario/cadastro"
    CADASTRO_PROPRIETARIO = "/proprietario/cadastro"
    CADASTRO_LOGIN = "/cadastro_login"
    CADASTRO_USUARIO = "/cadastro_usuario"
    LISTAGEM_IMOVEIS = "/listagem_imoveis"
    LOGIN = "/login"
    INICIO_DESLOGADO = "/inicio"
    INICIO_LOCATARIO = "/locatario"
    WELCOME = "/"
    CADASTRO_IMOVEL = "/cadastro_imovel"
    INICIO_PROPRIETARIO = "/proprietario"
    PERFIL_PROPRIETARIO = "/proprietario/perfil"
    EDITAR_PERFIL_PROPRIETARIO = "/proprietario/perfil/editar"
    PERFIL_LOCATARIO = "/locatario/perfil"
    EDITAR_PERFIL_LOCATARIO = "/locatario/perfil/editar"
    MOSTRAR_IMOVEIS_PROPRIETARIO = "/proprietario/imoveis"
    MOSTRAR_IMOVEL = "/imovel"
    VER_CONTRATO_ALUGUEL = "/locatario/contrato_aluguel"
    EDITAR_IMOVEL = "/proprietario/imovel/editar"
    DIARIAS = "/imovel/diarias"
    RELATORIO_ALUGUEIS = "/proprietario/relatorio_alugueis"
