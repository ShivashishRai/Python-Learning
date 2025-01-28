
#List : individual object as a single entity where insertion order preserved and duplicate is allowed

#ways to create and define list

ls = []   #create empty list

ls = [10,20,30]   #create list with know element

ls=range(10)      #create list with other DS

ls = eval(input("Enter list items: "))   #using dynamic inputs

#using split method
str = "Aston Martin"
ls = str.split( )
print(ls)

''' Access Elements '''

ls[0] # to access element at zero index
ls[-1] #to access last element of the list

#Slice
print(ls[::])   #start:end:step

#Traversing through all elements in the list

l = [13,15,18,21]
i = 0
while i < len(l):
    print(l[i])
    i = i+1
