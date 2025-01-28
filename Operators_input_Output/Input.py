

# fname= input("Enter first name:")
# lname = input("Enter last name:")
# salary= input("Enter emp salary:")    #entered integer but as input takes only string so can be overcome by using type casting
#
# print(type(fname))
# print(type(lname))
# print(type(salary))
#
# #Type Casting
#
# salary=int(input("Enter emp salary:"))
# print(type(salary))
#
# #eval data type
# # exp = int(input("Enter some expression: "))         #10+20+30/2+10
# # print(exp)                    #end up getting value error to overcome use eval line 20
# # print(type(exp))
#
#
# exp = eval(input("Enter some expression: "))             #10+20+30/2+10
# print(exp)
# print(type(exp))

# #Point to be noted
# lname=eval(input("Enter the Name"))            #Leading to an error in case user enter name in str type
#

# s= '22 24 27 30'      #user ented str type
# ls = s.split()         #by default split takes '' as seprator, in case user not entered
#
# print(ls)       #End up getting the list in str type
# print(type(ls))     #list data type
#
#
# #List Unpacing
#
# i , j, k = [11,12,13]
# print(i, end=" ")
# print(type(i))
#
# #example
# x= input("Enter two numbers to create a list: ").split()
# print(x)
# print(type(x))        #list data type but element present are in str format
#
# #to overcome str type
# x,y = input("Enter two numbers to create a list: ").split()    #Split is going to create a list and we have used list unpacking concept to get it into a int inplace of str
# print(x)
# print(y)
#
# # Tuple Unpacking
# i , j , k = (21,22,23)
# print(i, end=" ")
# print(type(i))


#List Comprehension

# a , b = [int (x) for x in input("Enter Two Values:").split()]
# print(type(a))

# num= [x for x in range(5)]
# print(num)
#
# i , j = [x for x in input("Enter first name and last name").split()]
# print(i)

i, j, k = [float(x) for x in input("Enter 3 no ro add: ").split(',')]
print("Sum of three number: ", i+j+k)