#
# #by adding two numbers
# a,b = 10,12
# sum=0
# sum=a+b
# print("The sum of two number is :",sum)
#
# #Adding user defined two numbers
# num1 = int(input("Enter the first positive number :"))
# num2 = int(input("Enter the second positive number :"))
# print("The sum of two number is :", end= "")
# addition = num1 + num2
# print(addition)
#
# #sum of two number with help of function
# def addtwonumbers(num1, num2):
#     defsum = num1 + num2
#     return defsum
#
# defsumtotal = addtwonumbers(31,49)
# print(defsumtotal)
#
# #add two number with lamda function
# lamdasum = lambda num1,num2 : num1+num2
#
# num1,num2 = 19 , 14
# sum_total = lamdasum(num1, num2)
#
# print("{} {}".format("Sum of two number with lambda function is :" ,+sum_total))


#Sum of two number with Recursive Function
def add_number_recurssive(num1, num2):
    if num2==0:
        return num1
    else:
        return add_number_recurssive(num1+1,num2-1)

num1,num2=151,191
recurssive_sum_total=add_number_recurssive(num1,num2)
print("The sum of two number with recurssive function is: ", recurssive_sum_total)

