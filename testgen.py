def odd():
    print('step 1')
    print(id(odd))
    yield 1
    print(id(odd))
    print('step 2')
    print(id(odd))
    yield 3
    print(id(odd))
    print('step 3')
    print(id(odd))
    yield 5

o=odd()
print(id(o))
next(o)
print(id(o))
next(o)
print(id(o))
next(o)
print(id(o))