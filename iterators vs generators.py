

#iterator
my_iter=iter(['My','Name','is','Shiv'])
print(type(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))



# my_tup_iter = (x for x in range(100))
# print(type(my_tup_iter))

#Example of a Generators in python

def sqr(n):
    for i in range(1,n+1):
        yield i*2

sqr_gen = sqr(5)
print(type(sqr_gen))
print(next(sqr_gen))
print(next(sqr_gen))
print(next(sqr_gen))
print(next(sqr_gen))
print(next(sqr_gen))
# print(next(sqr_gen))
# print(next(sqr_gen))

