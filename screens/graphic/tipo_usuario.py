import enum


class TipoUsuario(enum.Enum):
    PROPRIETARIO = "Proprietário"
    LOCATARIO = "Locatário"
    DESLOGADO = "Deslogado"
