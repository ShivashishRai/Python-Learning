
#Generators
'''
    It is a function
    it will generate sequence of values
    Generator will use yield keyword to generate value
'''

# gen_value = (x for x in range(1000000000000))
# print(type(gen_value))
#
# while True:
#     print(next(gen_value))


def my_gen():
    yield 'A'
    yield 'B'
    yield 'C'

values = my_gen()
# print(next(values))
# print(next(values))
# print(next(values))

for x in values:
    print(x)


