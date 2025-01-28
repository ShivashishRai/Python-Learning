
#Tuple : similar to list only difference is that its immutable

tup = ("Aston","Martin", "DB", 9 )
print(tup)
print(type(tup))

print(tup[2])       #accessing element of tuple
print(tup[1:3])     #tuple slicing

print(tup[-1])      #accessing last element of tuple

#tup[2] = "F6"           #uncommenting this will lead to an error as mentioned tulpe are immutable
#print(tup)

#Note : Single Value Tuple

tup=(10)
print(type(tup))     #will give it as int

#while defining single value tuple  , is mandatory to be mentioned
tup=(10,)
print(type(tup))

#to define the empty typle
tup = ()
print(type(tup))


import sys
tup = (10,'shiv','Hanuman',11,'Rama')
lst = [10,'shiv','Hanuman',11,'Rama']
print(sys.getsizeof(tup))
print(sys.getsizeof(lst))



x = range(10)
print(tuple(x))

#tuple creation with dynamic input from user
# tup = eval(input("Enter Elements into Tuple: "))
# print(tup)


#mATHMATICAL Operations on  tuple
t1 = ('Lambo','Umus','Camarro')
t2 = ('Volksvagen', 'Umus', ' Nissan')

t3 = t1 + t2
print(t3)

t3 = t1*2
print(t3)