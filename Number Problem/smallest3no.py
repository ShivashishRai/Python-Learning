
#Python Program to find Smallest number among three.

#Write a program in Python to find greatest among three integers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a < b and a < c:
    print(f"The smallest number among given number is :", a)

elif b < a and b < c:
    print(f"The smallest number among given number is :", b)

else:
    print(f"The smallest number among given number is :", c)

