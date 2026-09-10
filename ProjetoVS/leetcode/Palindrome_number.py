x = 158851

r_int = 0

while x > r_int:
    r_int = r_int * 10 + x % 10
    x = x // 10
print(x, r_int)
if r_int == x or x == r_int // 10:
    print('True')
else:
    print('False')
