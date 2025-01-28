
#Functions : A Group of repeated statements
        # Code Reusability
        # Concise Code

def calc(a,b):
    print("Addition :",a+b)
    print("Substraction :", a - b)
    print("Multiplication :", a * b)
    print("Division :", a/b)

calc(196,5)

# result = calc(196,5)
# print(result)


'''Type of Functions'''
#BUilt in Functions  - Python defined functions e.g. - len , type , id , eval etc.
#User Defined Functions - To meet our programming goal we crete function


# Function defined to take parameters at calling then user is bound to provide values else we will end up getting an Type Error

#WAP to take an argument from usr and print its square

def sqr(x):
    print("Square of given number is : ",x*x)

x=int(input("Enter number to get sqr: "))
sqr(x)

#WAP to print factorial of number of series

def fact(x):
    facto = 1
    if x != 1:
        while x>1:
            facto = facto*x
            x -=1
    else:
        pass
    return facto

for x in range(1):
    print("The Factorial of number {} is {},".format(x,fact(x)))
