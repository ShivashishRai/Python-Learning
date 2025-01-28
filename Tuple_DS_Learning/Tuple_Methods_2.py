
#Important Methods and Function used in tuple

tup = (10,'shiv','Hanuman',11,'Rama',10)

#len
print(len(tup))

#count
print(tup.count(10))

#index
print(tup.index('shiv'))     #better to first use membership operator

#sorted(python in buit function) : as sort method is not available in tuple so better use sorted and use type casting as sorted return in  list

tup=(11,2,17,9,6,13)
print(tuple(sorted(tup)))


#min
print(min(tup))

#max
print(max(tup))


#Note : Tuple Packing and Unpacking
a=10
b=13
c=12
d=1995

tup = a,b,c,d      #tuple packing  : values packed into a tuple
print(tup)

i , j, k, l = tup   #Tupple Unapacking : unpack the values from tup and assign it to i,j,k,l
print(i,j,k,l)

#WHEN variables are not as much as item in tuple we will be getting an Value error
# i , j = tup   #Tupple Unapacking : unpack the values from tup and assign it to i,j,k,l
# print(i,j,k,l)

#to over come above challenges we can use Group assignment
tup = (10,11,14,17,29,22,16,8,13)
a,b,c,d,*e = tup           #*e is Group assignment
print(a)
print(b)
print(c)
print(d)
print(e)

#Note: Tuple Comprehension is not applicable for Tuple as we end up getting Generators
tup = (x**2 for x in range(10))
print(type(tup))
