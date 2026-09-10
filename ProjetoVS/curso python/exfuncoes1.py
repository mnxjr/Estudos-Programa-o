

def multiplicar(*num):
    result = 1
    for i in num:
        result *= i
    return result
    

def par_impar(num):
    if num % 2 == 0:
        return f'O número {num} é par'
    return f'O número {num} é impar'
    

def criar_multiplicador(multiple):
    def multiplicador(num):
        return num * multiple
    return multiplicador

numeros = 7, 7, 3, 5 , 5, 3, 3
result = multiplicar(*numeros)
print(result)
print(par_impar(result))

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))
