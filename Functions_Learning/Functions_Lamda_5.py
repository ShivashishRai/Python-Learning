
#Annonyms Functions or Lambda Functions : Function without name
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
