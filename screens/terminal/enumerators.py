import enum


class TiposDeRespostas(enum.Enum):
    TEXTO = "texto"
    NUMERICO = "numerico"
    EMAIL = "email"
    SIM_OU_NAO = "sim_ou_nao"
