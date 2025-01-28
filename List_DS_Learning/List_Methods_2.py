
#List Methods

l = [10,20,33,10,43,51]

#len : length of the list
print(len(l))

#count : count of similar instace of element in the list
print(l.count(10))

#index : to know about the index of matching elemnt
print(l.index(33))

#append : to insert elemnt at last position
l.append(55)
print(l)

#insert : to insert elemnt ar specific position
l.insert(2,22)    #insert(index,element to be insert)
print(l)

#extend : add all elemnt of one list to the other list
l2=[33,34,37]
l2.extend(l)
print(l2)


#remove : to remove specific element present in the list i.e in case of multiple instances then only first occerance will be deleted
# in case elemnet not present in the list we want to removethen we will end up getting value error
l2.remove(33)
print(l2)

#pop : to delete specific element from the list by default last element from the list will be deleted
# in case pop operation is performend on empty list this will lead to Index Error
print(l2.pop())      #by default last element pop  i.e pop(index)
print(l2.pop(2))     #pop 2nd index element from the list
print(l2)

# #clear : to remove all element from the list
# l.clear()
# print(l)
#
# l2.clear()
# print(l2)

#reverse
l2.reverse()
print("Reverse: ", l2)

#sort :
l2.sort()
print(l2)

l2.sort(reverse=True)
print("Sort in reverse order: ",l2)