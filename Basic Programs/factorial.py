
#WAP to print factorial of given number

#Trick 1 : using the recursive function
# def factorial(x):
#     if x==0 or x==1:
#         return 1
#     else:
#         return x * factorial(x-1)
#
# numb = int(input("Enter the number to get the factorial as an output: "))
#
# result = factorial(numb)
# print(f"The factorial of the {numb} is {result}")

#Trick 2 : using the while loop iterator in function

def factorial(numb):
    fact = 1
    if numb <0:
        return 0
    elif numb ==0 or numb ==1:
        return 1
    else:
        while numb >1:
            fact *= numb
            numb -= 1
        return fact

numb = int(input("Enter the number to get the factorial as an output: "))
result = factorial(numb)
print(f"The factorial of the {numb} is {result}")