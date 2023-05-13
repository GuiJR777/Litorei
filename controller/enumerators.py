import enum


class ComandoUsuario(enum.Enum):
    LISTAR_IMOVEIS = "listar imoveis"
    SAIR = "sair"
    VOLTAR = "voltar"
    CADASTRAR_USUARIO = "cadastrar usuario"
    LOGAR_USUARIO = "logar usuario"
    CADASTRAR_LOCATARIO = "cadastrar locatario"
    CADASTRAR_PROPRIETARIO = "cadastrar proprietario"
    IR_CADASTRO_LOGIN = "ir cadastro login"
    VER_PERFIL_LOCATARIO = "ver perfil locatario"
    VER_CONTRATOS_LOCATARIO = "ver contratos locatario"
    VER_PERFIL_PROPRIETARIO = "ver perfil proprietario"
    VER_IMOVEIS_PROPRIETARIO = "ver imoveis proprietario"
    CADASTRAR_NOVO_IMOVEL = "cadastrar novo imovel"
    EDITAR_PERFIL_PROPRIETARIO = "editar perfil proprietario"
