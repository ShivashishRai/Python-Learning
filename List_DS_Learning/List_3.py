
#Aliasing and Cloning

#Aliasing :process of creating duplicate reference variable is called aliasing
l1 = [10,12,18,22,27]
l2 = l1
l1[1] = 25
print(l2)
print(id(l1))
print(id(l2))


#Cloning : process of creating duplicate object is called cloning

l1=[17,19,21,22,28]
l2 = l1[:]

l2[1] = 25
print(l1)
print(l2)
print(id(l1))
print(id(l2))

#Mathmatical OPERATORS

l1 = [11,13,15,17]
l2 = [14,16,18,20]

'''
+: Opetor creats a new and return the object
extend : new object won't be created exexsting object only.
'''


#Nested List : List inside another list
l1 = [11,14,17, [18,21,24]]
print(l1[3])   #[18,21,24]
print(l1[3][2])  #24

#Multi dimensional Array
l1 = [[11,12,13],[17,18,19],[21,22,23]]
print("Element present row wise: ")
for x in l1:
    print(x)

print(l1[2][2])

   #print multi dimensional array in matrix style

for x in l1:
    for y in x:
        print(y, end=' ')
    print()

