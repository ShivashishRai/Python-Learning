#Trick 1 using the function

#Funcion to add two number
def addition(num1,num2):
    sum_total = num1 + num2
    return sum_total                        #returning the computed value to the function call


#asking user to input number for addition
num1 = int(input("Enter the first number to Addition: "))
num2 = int(input("Enter the second number to Addition: "))

#calling the function with arguments received from user
print(f"The Sum total of the number is: {addition(num1,num2)}")

#Trick 2 using lambda function

#Addition of two number with lambda suntion

addition_lambda = lambda num1, num2 : num1 + num2   #lamda expression takes 2 argumnet and one expression

addition_value = addition_lambda(num1,num2)        #calling the lamda function to compute two value
print(f"Sum total of two value usking lambda is {addition_value}")