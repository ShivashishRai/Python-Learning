
#Set Maathmatical Operators and Comprehension

#   + ,* are not valid for set
se1 = {10,20,30}
se2={'Rama','Sita','Laxman'}

#se3 = se1+se2   #We will end up getting TypeError as it's unsupported operation
#se4 = se1*3      #We will end up getting TypeError as it's unsupported operation

#Mathmatical Operation available under set's are as follows

#Union : Common elemnt b/w two sets
se1 = {17,18,22,11}
se2 = {22,19,21}

print(se1.union(se2))

#intersection : as name suggest it fetches only common element from both sets
print(se1.intersection(se2))

#difference : as name suggest it featches unique element b/w two sets
print(se1.difference(se2))

#sematical_difference : elements from both the sets except the common b/w both sets
print(se1.symmetric_difference(se2))


#Membershop Operators
#in and not in is applicable similar to other DS we have covered



#Set Comprehension : similar to list set also support comprehension below is an example

se_comp = {x for x in range(10) if x %2!=0 }
print(se_comp)





