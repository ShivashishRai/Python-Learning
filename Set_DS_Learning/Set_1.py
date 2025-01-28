
#Set Data Structure
'''
Duplicate objects not allowed and order is not preserved , indexing and slicing not allowed ,  Mutable and growable in nature
'''

se = {10,13,16,12,13,18,9,5,13,18}    #Entered duplicate element intentionally
print(se)

se = [10,13,16,12,13,18,9,5,13,18]
print(set(se))                       #Type casting list into set data structure

se = set(range(9))
print(se)

dict = {100:"Shiva",202:"Rama", 303:"Sita"}
print(set(dict))

dict = {"Shiva":100,"Rama":204, "Sita":404}    #Only keys are consder from dictionary
print(set(dict))

se = eval(input("Enter values into a set: "))
print(se)



#Note: Empty Set Object
se = {}
print(type(se))   #it's going to be dict and not set as by default {} are consider as dict and not set, to make empty set define as below

se = set()        #to create an empty set as set is by default python function and not method
print(type(se))


#Imporatnt methods of set

se.add(12)       #add can take up only one argument
# se.add(10,20,30)                #uncommenting this code will lead to an error as mentioned above add takes up only one argument
se.add(10)
se.add(12)
se.add("Ferrari")
print(se)

#Update : can be added as sequence and not an individual elemnts, this overcome challenges of add
se.update(range(0,8), 'Rama', ' Raja', 'This')
print(se)

#Note
#se.update(10,) #is not valid as 10, is treated as single argument where as update method expect to enter sequence of char
se.update((10,))  #is valid statement as it form sequence of tuple
print(se)

#Note : set uses hashable concept for storing the element

#int, float , str , tuple : are hashable
#list is not hashable

se.add(10)   #Valid statement
se.add('Astor')
se.add(11.89)

#se.add([15,16,17])    #invalid as mentioned list is unhashable
#print(se)

#se.add([19,20,21])     #Invalid as we are adding list element directly and list is unhashable
se.update([19,20,21])  #valid as we are not adding list object directly, we are adding element present in list.

#Note
#se.update([19,20,[21,22]])   #will lead to an error as we are trying to add list [21,22] amd its unhashable as mentioned that will lead to an error

#se.set([19.20,21])     #valid as we are not adding list object directly, we are adding element present in list.

print(se)


#Remove and element from set

#pop : it removes and return  random element from set incase we attempt to remove from an empty set then we will end up getting KeyError from PVM
se.pop()
print(se)

#remove : it removes the particular element from set in case specified element not in set then we will end up getting KeyError
se.remove('Astor')
print(se)

#discard : it removes the particular element from set in case specified element not in set then we won't end up getting KeyError like remove(mentioned above)
se.discard('Blazy')
print(se)


#clear : similar to list it clear all element present in set
se.clear()
print(se)







