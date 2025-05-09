from categoria import Categoria
from transacao import Transacao

LISTA_CATEGORIAS = []
LISTA_TRANSACOES = []

def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome)
    LISTA_CATEGORIAS.append(nova_categoria)
    return nova_categoria

def cadastrar_transacao(descricao, valor, categoria):
    nova_transacao = Transacao(descricao, valor, categoria)
    LISTA_TRANSACOES.append(nova_transacao)
    return nova_transacao

def saldo_total():
    total = 0
    for transacao in LISTA_TRANSACOES:
        if transacao.categoria.nome == "Receitas":
            total += transacao.valor
        elif transacao.categoria.nome == "Despesas":
            total -= transacao.valor
        elif transacao.categoria.nome == "Viagens":
            total -= transacao.valor
    return total