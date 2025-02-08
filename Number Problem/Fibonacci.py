#Write a program in Python to print the Fibonacci series using iterative method.

Numb = int(input("Enter the Number for printing fibonacci: "))
print(f"The number for fibonacci opted by user is : ", Numb)

first_Numb = 0
second_Numb = 1
fib_sum = 0

for x in range(0,Numb):
    if Numb == 0:
        print(f"Fibonacci of the Number is ",{Numb})
        break
    elif Numb == 1:
        print(f"Fibonacci of the Number is ", {Numb})
        break
    else:
       fib_sum = first_Numb + second_Numb
       first_Numb = second_Numb
       second_Numb = fib_sum
print(f"The Fibonacci series of the {Numb} is :", fib_sum)