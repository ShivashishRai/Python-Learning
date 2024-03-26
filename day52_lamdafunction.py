
square = lambda x : x**2

Avg = lambda x,y,z : (x+y+z)/3

print(square(5))
print(int(Avg(11,12,13)))


is_even = [lambda arg = x : arg *2 for x in range(1,11)]
for num in is_even:
    print(num())

#Maxium b/w two numbers
max_num = lambda a,b : a if (a>b) else b
print("Max number is", max_num(21,28))


#convert string to upper case letter with help of lamda function
name="Shivashish"
name_upper = lambda name : name.upper()
print(name_upper(name))


#passing function as an arguments to another function
