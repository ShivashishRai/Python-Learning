
Numb=int(input("Enter the Number to check Armstrong: ",))

power = len(str(Numb))       #count the number of digits in the number for power computational
digit=0                      # for Getting the digits of the number
Sum_value=0                  # Storing the sum value of the computation
temp=Numb                    # to iterate over the number

while temp >0:                          # loop on each digit of number and get their sum
    digit = temp%10
    Sum_value=Sum_value + digit**power
    temp = temp//10
# print(Sum_value)
if Numb == Sum_value:                     #Compare sum digit with number to validate armstrong
    print(f"The Number {Numb} is Armstrong Number")

else:
    print(f"{Numb} is not Armstrong number !! Better luck Next time")
