# Exercícios

from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print('PRODUTOS ORIGINAIS\n')
print(*produtos, sep='\n')

# Gere novos_produtos por deep copy (cópia profunda)
# Aumente os preços dos produtos a seguir em 10%
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in deepcopy(produtos)
]
print('\nPRODUTOS COM AUMENTO DE 10% NO PREÇO\n')
print(*novos_produtos, sep='\n')

# for p in novos_produtos:
#     aumento_10 = p['preco'] * 1.1
#     p['preco'] = float(f'{aumento_10:.2f}')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)
print('\nPRODUTOS ORDENADOS(decrescente) POR NOME\n')
print(*produtos_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    deepcopy(produtos),
    key=lambda p: p['preco']
)
print('\nPRODUTOS ORDENADOS POR PRECO\n')
print(*produtos_ordenados_por_preco, sep='\n')
