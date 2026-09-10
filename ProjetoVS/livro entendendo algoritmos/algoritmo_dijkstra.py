def ache_o_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo<custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

grafo = {}

grafo['inicio'] = {}
grafo['inicio']['A'] = 6
grafo['inicio']['B'] = 2

grafo['A'] = {}
grafo['A']['Fim'] = 1

grafo['B'] = {}
grafo['B']['A'] = 3
grafo['B']['Fim'] = 5

grafo['Fim'] = {}

custos = {}

infinito = float('inf')

custos['A'] = 6
custos['B'] = 2
custos['Fim'] = infinito

pais = {}

pais['A'] = 'inicio'
pais['B'] = 'inicio'
pais['Fim'] = None

processados = []


nodo = ache_o_custo_mais_baixo(custos) # B

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_o_custo_mais_baixo(custos)
