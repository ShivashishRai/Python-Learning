
'''
map function ----> for every input valur, generate output value based on some operations
i.e. increment 10% salary of each input current salary
i.e. find square of 10 numbers

'''

#WAP to square each value with help of map and lamda expression

sqr = [2,5,7,11,14,16,19]

lam_sqr = list(map(lambda x:x*x,sqr))
print("The square of each given number is:",lam_sqr)
