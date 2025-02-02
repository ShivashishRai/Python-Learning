
tup = ('Shiv', 'Champaran', 700 , 'INR', (1800,1200,1300),['Gaytri','Rai', 'Tiwari'])
tup1 = ('Akshat', 'Kumar','Shreyash', 'Pal')
print(len(tup))
conc_tup = tup1+tup
print(conc_tup)

print(conc_tup[9].count('Rai'))

list_element = list(tup)
# list_element.sort()
print(list_element)

list_element.pop(3)
list_element.append("Sexy")

tup = tuple(list_element)
print(tup)

