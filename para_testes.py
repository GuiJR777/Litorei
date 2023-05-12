'''
ESTE ARQUIVO É APENAS PARA TESTES

Depois deve ser apagado e retirado dos imports (ver ToDo's nos arquivos)
'''

from model.enumerators import StatusImovel, TipoProprietario
from model.imovel import Imovel
from model.locatario import Locatario
from model.proprietario import Proprietario


locatarios = [
    Locatario(
        "João da Silva",
        "joao@email.com",
        "5548987654321",
        "senha123",
        "09876543210",
    ),
    Locatario(
        "Maria da Silva",
        "maria@email.com",
        "5548987654321",
        "senha123",
        "09876543210",
    ),
]

proprietarios = [
    Proprietario(
        "Zé Ricão",
        "ze@email.com",
        "5548987654321",
        "senha123",
        "09876543210",
        TipoProprietario.PESSOA_FISICA,
    ),
    Proprietario(
        "Imobiliária Zé Ricão",
        "contato@zericão.com",
        "5548987654321",
        "senha123",
        "09876543210",
        TipoProprietario.PESSOA_JURIDICA,
    ),
]

imoveis = [
    Imovel(
        "Linda casa no centro",
        "Centro, nº 123",
        250.00,
        "proximo a beira-mar",
    ),
    Imovel(
        "Apartamento no centro",
        "Centro, nº 123",
        250.00,
        "proximo a beira-mar",
    ),
    Imovel("Casa na praia", "Praia, nº 123", 350.00, "proximo ao mar"),
    Imovel(
        "Apartamento na praia", "Praia, nº 123", 350.00, "proximo ao mar"
    ),
]

proprietarios[0].adicionar_imovel(imoveis[0])
proprietarios[1].adicionar_imovel(imoveis[1])
proprietarios[1].adicionar_imovel(imoveis[2])
imoveis[3].status = StatusImovel.ALUGADO
proprietarios[1].adicionar_imovel(imoveis[3])
