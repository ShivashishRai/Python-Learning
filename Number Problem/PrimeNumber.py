

check_prime=int(input("Enter the number to check prime or not: "))
temp = 0
if(check_prime > 1):
    for x in range(2,check_prime//2):
        if(check_prime%x ==0):
            temp = 0
            break
        else:
            temp = 1
    if(temp==0):
        print(f"The number {check_prime} is not prime number")
    elif(temp==1):
        print(f"The number {check_prime} is a prime number")

else:
    print("Please Enter the positive number to check prime number")