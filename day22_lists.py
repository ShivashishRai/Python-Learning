
class10maths = [33,28,48,88,62,(39,58,79),[19,4],['Shiv','Ashish','Rai']]

print(class10maths[7][1])
print(type(class10maths))
print(type(class10maths[5]))

print(class10maths[-3][2])
print(class10maths[len(class10maths)-1][0])

#to identify wheather 66 is found in the tuple present in the list of element
if 66 in class10maths[5]:
    print("Found")
else:
    print("Not Found")

#to iterate over the each element added in the tuple present in the list of elements
for x in class10maths[5]:
    print(x)


print(class10maths[4:-2])

#List comprehension problems
comp = [x**2 for x in range(10) if x%2 !=0 ]
print(comp)


#More examples of list comprehension

table=[2,5,7,11,14]
double = [x*2 for x in table]
print(double)

#nested loop in list comprehensoion
complexcompre = [[z for z in range(6)] for y in range(4)]
print(complexcompre)