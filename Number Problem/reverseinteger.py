
#Write a program to reverse an integer in Python.
#    Input : 321
#   Output : 123

num = int(input("Input the number for reversal: ",))
print("The Number before reversal: ",num)

rev_num = 0                     # Iitally reversal number is 0
while num>0:                    # till the number computational is greater then 0
    rev_num = rev_num*10 + num%10     # Generating reversal of the number
    num = (num//10)                   # Getting floor Quoitent of the Number

print(f"The Reverse of the number is :", rev_num)

