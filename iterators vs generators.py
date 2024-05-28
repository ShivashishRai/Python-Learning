

#iterator

my_iter=iter(['My','Name','is','Shiv'])
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


#Example of a Generators in python

try:
    def sqr(n):
        for i in range(1,n+1):
            yield i*2

    sqr_gen = sqr(5)
    print(next(sqr_gen))
    print(next(sqr_gen))
    print(next(sqr_gen))
    print(next(sqr_gen))
    print(next(sqr_gen))
    print(next(sqr_gen))
    print(next(sqr_gen))

except StopIteration as SI:
    print(SI)
