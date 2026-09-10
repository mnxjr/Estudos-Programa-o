def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)
    

def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

def contador(lista):
    if lista == []:
        return 0
    return 1 + contador(lista[1:])


def maximo(lista):
    # if lista == []:
    #     return 0
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

def quicksort(array):
    if len(array) < 2:
        print(f'Array: {array}\n')
        return array
    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]
    print(f'Maiores: {maiores}'
          f'\nMenores: {menores}'
          f'\nPivo: {pivo}\n')
    return quicksort(menores) + [pivo] + quicksort(maiores) 

a1 = [1,2,3,5,100, 1 , 55, 19, 13,44,99,0]
print(quicksort(a1))