import enum


class ComandoUsuario(enum.Enum):
    LISTAR_IMOVEIS = "listar_imoveis"
    SAIR = "sair"
    VOLTAR = "voltar"
    CADASTRAR_USUARIO = "cadastrar_usuario"
    LOGAR_USUARIO = "logar_usuario"
    CADASTRAR_LOCATARIO = "cadastrar_locatario"
    CADASTRAR_PROPRIETARIO = "cadastrar_proprietario"
    IR_CADASTRO_LOGIN = "ir_cadastro_login"
    VER_PERFIL_LOCATARIO = "ver_perfil_locatario"
    VER_CONTRATOS_LOCATARIO = "ver_contratos_locatario"
