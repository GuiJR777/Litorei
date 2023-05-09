import enum


class ComandoUsuario(enum.Enum):
    LISTAR_IMOVEIS = "listar_imoveis"
    SAIR = "sair"
    CADASTRAR_USUARIO = "cadastrar_usuario"
    LOGAR_USUARIO = "logar_usuario"
    CADASTRAR_LOCATARIO = "cadastrar_locatario"
    CADASTRAR_PROPRIETARIO = "cadastrar_proprietario"
