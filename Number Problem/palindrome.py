
#Write a program in Python to check whether a number is palindrome or not using iterative method.

#    Input : 321
#   Output : 123

num = int(input("Input the number for reversal: ",))
print("The Number before reversal: ",num)
temp = num
rev_num = 0                     # Iitally reversal number is 0
while temp>0:                    # till the number computational is greater then 0
    rev_num = rev_num*10 + temp%10     # Generating reversal of the number
    temp = (temp//10)                   # Getting floor Quoitent of the Number

print(f"The Reverse of the number is :", rev_num)
if num == rev_num:
    print(f"The given Number {num} is a Palindrome")
else:
    print(f"The given Number {num} is not a Palindrome")