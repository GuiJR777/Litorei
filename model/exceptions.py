class JaPossuiAluguelException(Exception):
    super().__init__("O cliente já possui um aluguel em aberto.")


class ImovelIndisponivelException(Exception):
    super().__init__("O imóvel está indisponível para aluguel.")


class NaoPossuiImovelAlugadoException(Exception):
    super().__init__("O cliente não possui um imóvel alugado.")


class ImovelNaoEncontradoException(Exception):
    def __init__(self, identificador: str) -> None:
        super().__init__(
            f"O imóvel com identificador {identificador} não foi encontrado."
        )
