
#Write a program in Python to swap two number without using third number

first_num = int(input(f"Enter the first Number: "))
second_num = int(input(f"Enter the second Number: "))

first_num = first_num - second_num
second_num = first_num + second_num
first_num = second_num - first_num

print(f"The first number after swapping is : ",first_num)
print(f"The second number after swapping is : ",second_num)

