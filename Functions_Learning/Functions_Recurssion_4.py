
#Recursive Function : Function that call itself is known as Recursive Function.

def factorial(n):
    if n==0:
        result=1
    else:
        result = n * factorial(n-1)
    return result

print(factorial(8))