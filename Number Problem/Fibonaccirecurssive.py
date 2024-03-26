
#Write a program in Python to print the Fibonacci series using recursive method.

fib_sum = 0
def fibonacci(num):
    first ,second = 0,1
    if num == 0:
        return 0
        #print(f"Fibonacci of the Number is ",{num})

    elif num == 1:
        return 1
        #print(f"Fibonacci of the Number is ", {num})
    else:
       fib_sum = num-1 + num-2
       return fib_sum

Numb = int(input("Enter the Number to calculate Fibonacci with recurssive method: "))
for i in range(0,Numb):
    print(f"The Fibonacci series is :",fibonacci(i))

