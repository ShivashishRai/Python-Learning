
#Dictionary: to represent group of object as {Key:Value} pair
      #Duplicate keys are not allowed but values are allowed

#Mutable,Order is not applicable and all element will be insrted based on hash of keys , Slicing and Indexing applicable , Allow Hetrogenous object for both keys and values ,
  # i.e. in case specified key is already present then old value will be replaces with new value

mydict = {}
#mydict = dict()    #another way to define dict

print(type(mydict))

#to enter value into an empty or existing dictionary
mydict[101] = 'Shankar'
mydict[102] = ' Birla'
mydict[103] = 'Shekhar'
mydict[104] = 'Raju'


print(mydict)
#mydict = {101:'Shankar',102:'Birla',103:'Shekhar',104:'Raju'}

#How to access value through the key
print(mydict[103])

#Note :  in case key is not present in dictionary then we will end up getting an Key Error
# print(mydict[106])         #keyError as 106 key is not present in mydict

#to overcome above keyError we can cater this by Membership oerator similar
