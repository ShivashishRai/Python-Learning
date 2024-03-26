

def adds(num1,num2):
    result = num1 + num2
    return result

def subs(num1, num2):
    if num1 > num2:
        result = num1 - num2
    else:
        result = num2 - num1

    return result

def mults(num1, num2):
    result = num1 * num2
    return result

def divs(num1, num2):
    result = num1 / num2
    return result

def floorval(num1, num2):
    result = num1 // num2
    return result

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

endresult = subs(num1,num2)
print("The result value is: ",endresult)
