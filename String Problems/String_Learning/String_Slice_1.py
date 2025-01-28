
# #String : Any sequence of char
#
# ''' Usage
# 1. to define multi line string literals
# 2. single or double quotes as symbol
# 3. doc string
# '''
#
# #Slice Operator -- used to access string characters
# #Slice operator never raise an index error
#
# name = "Shivashish"
# print(name[2:6])         #start position - 2 :end position - 6
# print(name[5:])          #start position - 5 :end position - end of string
# print(name[:])           #start position - start of string :end position - end of string
# print(name[:-4:-1])
# print(name[2:9:2])       #start position - 2 :end position - 9 : Step - 2
#
#
# #WAP to print positive and negative index with char
# word = input("Enter the Word: ")
# i=0
# word_len = len(word)
# for x in word:
#     print("The Char present at positive index {} and at negative index {} is {}".format(i,i-word_len,x))
#     i +=1
#
# #strip  lstrip rstrip
#
# #index
#
# #find
#
# #Count
#
# #replace
# org = input("Enter the Original String: ")
# mod = input("Enter the sub string to be replaced in org string: ")
# updated = org.replace(' ',mod)
# print(updated)
# print(len(org)-len(updated))
#
# #Split
# sp = "Aston Martin"
# l = sp.split(' ')
# for x in l:
#     print(x)

#Join
class_name = ['Sunny', 'Leone' , 'Sunny','Deol', 'Bobby','Deol']
jo = '-'.join(class_name)
print(jo)

marks = ('10','20','30')
up_marks = ''.join(marks)
print(up_marks)

#Change the case of string
'''
Upper
Lower
swapcase
title
capitalize
'''

str= "mahindra launched xuv 700 and it is going to blow other comanies"
print(str.upper())
print(str.lower())
print(str.title())
print(str.capitalize())


#in case you want to check char present in given string
'''
isalnum
isalpha
isdigit
islower
isupper
istitle
isspace
'''

str = "Aston Martin DB"
print('AstonMartin786'.isalnum())
print(str.istitle())
print(str.isupper())
print('astonmartindb7'.islower())


