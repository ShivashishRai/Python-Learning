
import math

#Program to find wheather the number is prime or not without using math library
check_num = int(input("Enter the number you want to check prime :"))
if check_num == 0 or check_num ==1:
    print(f"{check_num} is prime")

else:
    for i in range(2,int(check_num//2)+1):
        if check_num %i !=0:
            print(f"{check_num} No is a Prime number")
            break

    else:
        print(f"{check_num} is not Prime Number")


#identify no is prime or not using math library

def prime_no(num):
    if num<=1:
        print("No is not prime")
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                print(f"Number is not prime {num}")
        else:
            print(f"{num}No is a prime no: {num}")



result = prime_no(check_num)

