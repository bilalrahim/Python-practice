
 #a generator function that returns an
 #object (iterator) which we can iterate over (one value at a time).

def squar(lis):

    for i in lis:
        yield i*i






sq=squar([1,2,3,4])

for i in range(4):
    print next(sq)
