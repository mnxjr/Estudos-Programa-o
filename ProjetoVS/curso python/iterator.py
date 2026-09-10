txt = 'Vasco'
iterador = iter(txt)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration as erro:
        print(erro)
        break

lista = [['edson', 'junior', 'de', 'oliveira', 'muniz'],['erica', 'lorrayne'], ['hellen', 'muniz']]
print(*lista[lista])
