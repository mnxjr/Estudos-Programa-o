from collections import deque


grafo = {}
grafo['voce'] = ['alice', 'bob', 'claire']
grafo['bob'] = ['anuj', 'peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['thom', 'jonny']
grafo['anuj'] = []
grafo['peggy'] = []
grafo['thom'] = []
grafo['jonny'] = []


def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'


fila_de_pesquisa = deque()
fila_de_pesquisa += grafo['voce']

while fila_de_pesquisa:
    
    pessoa = fila_de_pesquisa.popleft()

    if pessoa_e_vendedor(pessoa):
        print(f'{pessoa} é um vendedor de manga!')

    else:
        fila_de_pesquisa += grafo[pessoa]
