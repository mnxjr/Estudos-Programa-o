# Variáveis livres + nonlocal (locals, globals)
'''A declaração global sempre faz referência ao escopo global, isto é, o escopo do
   programa, em si, enquanto a nonlocal referencia o escopo local acima do escopo
   atual.'''

# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

# > globals <
def concatenar(string_inicial):
    # > nonlocal <
    valor_final = string_inicial 

    def interna(valor_a_concatenar=''):
        nonlocal valor_final # nonlocal  referencia o escopo local acima do escopo atual
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)