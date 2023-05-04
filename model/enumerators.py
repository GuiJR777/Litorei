import enum


class StatusImovel(enum.Enum):
    ALUGADO = "Alugado"
    DISPONIVEL = "Disponível"
    INDISPONIVEL = "Indisponível"


class TipoLocador(enum.Enum):
    PESSOA_FISICA = "Pessoa Física"
    PESSOA_JURIDICA = "Pessoa Jurídica"
