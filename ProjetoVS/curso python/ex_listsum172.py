from itertools import zip_longest

listaA = [5, 9, 22, 3, 14]
listaB = [11, 7 ,31, 6, 8, 33, 12, 4]
soma_AeB = [x + y for x, y in zip_longest(listaA, listaB, fillvalue=0)]
print(soma_AeB)

filtlist = [i for i in soma_AeB if i < 15]

print(filtlist)