from pandas import DataFrame

a = [[1, 2, 3], [4, 5 ,6], [7, 8, 9]]

df = DataFrame(a, columns='A B C'.split(), index='l1 l2 l3'.split())

print(df['B', 'l1'])