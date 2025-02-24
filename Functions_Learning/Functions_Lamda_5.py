
#Annonyms Functions or Lambda Functions : Function without name
             # We can pass function as an argument to another function there we lambda function is best suitable.
             #no def keyword is required nor any return statement

             # Syntax - lambda arguments : expression

#Square of number through lambda function
sqr = lambda x : x*x
print(type(sqr))
num = int(input("Enter the number to square: "))
print("Square of number is :",sqr(num))

#Largest b/w 2 nuumbers

big = lambda a,b : a if a >b else b
print("Largest of two number is :",big(18,23))


#Largest of three number using lambda function

large_3 = lambda a,b,c : a if a > b and a>c else b if b>c else c
print("Largest of three number is : ", large_3(17,25,9))


#Filter() :  utilised for filtering value from given sequence based on some condition
        #Syntax - filter(function,sequence)

lis = [13,14,18,27,28,33,37,41,44,24]
my_even =list(filter( lambda x : x %2 ==0, lis))
my_odd = list(filter( lambda x : x %2!= 0,lis))
print(my_even)
print(my_odd)

#WAP to get strings with length greater than 4 using lamda filter function
my_str = ('Anu','Priya','Sikha','Ishu','Apu','Aman')

len_4 = filter(lambda x :len(x) >4, my_str)
print(type(len_4))
print(tuple(len_4))



from functools import reduce

# Example: Find the product of all numbers in a list
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)
