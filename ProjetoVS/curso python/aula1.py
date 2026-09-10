

def g(n=0, maximum=1000):
    yield 1
    yield 2
    yield 3 
    yield 4
    yield 6
        

gen = g()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
