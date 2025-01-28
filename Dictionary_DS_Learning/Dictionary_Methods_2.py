


#WAP to enter student name and marks till user wants to wishes to continue

# dic = {}
#
# while True:
#     name = input("Enter name of the student: ")
#     marks = int(input("Enter Student marks : "))
#     dic[name] = marks
#
#     option = input("Do you wish to continue Yes|No : ")
#     while option.lower() not in ['yes','no']:
#         option = input("Entered value is invalid please enter valid input: ")
#     if option.lower() == 'no':
#         break
#
# print(dic)
#
# print('Name \t \t Marks')
# print('#'*15)
# for x in dic:
#     print(x, '\t \t' , dic[x])
# print('#'*15)


mydict = {101:'Shankar',102:'Birla',103:'Shekhar',104:'Raju'}
#Delete elements from dictionary
del mydict[104]            #in case specified key is not present for deleteion then we will end up getting KeyError on screen
print(mydict)

#clear : to clear all the element present in the dict similar to list and tuple

#Useful Methods of dictionry data structure
mydict = dict([(100,'Aston'),(200,'Martin'),(303,'DB9')])     #list of tuples to type cast into dict
print(mydict)

mydict = dict(((100,'Aston'),(200,'Martin'),(303,'DB9')))     #tuple of tuples to type cast into dict
print(mydict)

mydict = dict([[100,'Aston'],[200,'Martin'],[303,'DB9']])     #list of list to type cast into dict
print(mydict)

# mydict = dict({[100,'Aston'],[200,'Martin'],[303,'DB9']})     #it is an invalid as mentioned list is not hashable --- set of list to type cast into dict
# print(mydict)

#len : to get the length of the dictoinary or number of key value pair of dictionary
print(len(mydict))

#get : return corresponding value and in case key is not present then we will not get key error it will get 'None' as return
print(mydict.get(100))           #this will fetch value against key:100 from mydict dictionary and in case keys not  present then as mentioned it will display 'None' and no error will appear on screen
print(mydict.get(400,'Ram'))     #default value in case key is not present

#pop : (key-value pair) remove item associated with item
mydict.pop(100)      #in case specified key not avialbel then we will be getting keyError
print(mydict)

#popitem : it remove an arbitory item from the dictionary
print(mydict.popitem())
print(mydict)

#keys : to fetch only keys of dictionary
mydict[313]="Rinki"
mydict[343]="Sachiv G"

my_keys = mydict.keys()
print(type(my_keys))
print("Keys :",my_keys)

for x in mydict.keys():
    print("Keys :",x)

#Values : to fetch only values of dictionary
print("Values: ",mydict.values())

for val in mydict.values():
    print("All Values are:",val)

#items : key value pair

all_items = mydict.items()
print(all_items)

for x in all_items:
    print(x)

for ke , val in mydict.items():
    print('Keys - {} : Value - {}'.format(ke,val))


#setdefault : if specified key is already avalable then it return corresponding value, whereas in case specified key not available then provided key value pair will be added as new items in dictionary.
            #only one ket value can be added at times by setdefault method

print(mydict.setdefault(200,"Urus"))     #key is already present so we will be getting exiting item
print(mydict.setdefault(441,"Bikas"))    #as key is not part of existing items so new key value will be added to dictionary and it return the added value
print(mydict)

#Update : In order to add one dictionary to an another one we can do this by update method, we can say update can be used for dictinary concatination

mydict1 = {212: "Nihal", 450: 'Raina',490:'Loves',555:'Bike'}

mydict.update(mydict1)      # Note: all key values of mydict1 will be added to mydict dictionary
print(mydict)        #in case keys are already present then it will be updated with the latest value as i have mentoined above

#copy : Cloning
mydict2 = mydict.copy()    #this create new object mydict2
print(mydict2)

print("Id of mydict is: ",id(mydict))
print("Id of mydict is :",id(mydict2))     #reference id would be both different of both the object


#WAP To get frequency of word from a string

word_dic = input("Enter the Word to get the frequency: ")
word_dic_split = word_dic.split()
freq_dic = {}

#     #Solution 1 :Basic solution and logic to be applied
# for x in word_dic_split:
#     if x in freq_dic:
#         freq_dic[x] = freq_dic[x]+1
#     else:
#         freq_dic[x] =1
#
# print("Word Frequency is as follows :",freq_dic)
# print(max(freq_dic.values()))

    #solution 2 : Intermidiate Solution
for x in word_dic_split:
    freq_dic[x] = freq_dic.get(x,0)+1

print("Word Frequency is as follows :",freq_dic)
print(max(freq_dic.values()))


#WAP to get the count of vowels in a char
word_dic = input("Enter the Word to get the frequency: ")
freq_vow_dic = {}

for x in word_dic:
    if x in ['a','e','i','o','u']:
        freq_vow_dic[x] = freq_vow_dic.get(x,0)+1

print(" Frequency of vowels is as follows :",freq_vow_dic)
