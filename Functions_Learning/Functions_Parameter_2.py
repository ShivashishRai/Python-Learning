
#Functions with Parameters

#Types of Arguments :

#1. Positional Arguments
#2. Keyword Arguments
#3. Defauly Arguments
#4. Variable Length Arguments

#Positional Arguments example : number of arguments must match and ordeder of the argument is also very critically important
def calc(a,b):
    print("Addition :",a+b)
    print("Substraction :", a - b)
    print("Multiplication :", a * b)
    print("Division :", a/b)

calc(196,5)     #in case we would have passed only one argumnt then we would ended up getting an Type Error cum Positional


#Keyword Arguments : pass argument value by keyword i.e. by parameter name e.g.
                # number of arguments must match where as here order is not important unlike positional argymnets
def calc(a,b):
    print("Addition :",a+b)
    print("Substraction :", a - b)
    print("Multiplication :", a * b)
    print("Division :", a/b)

calc(a = 77,b= 18)
calc(b=27, a=18735)


# Imprtant Note : if in case you want to use both positional and keyword arguments then you must first pass positional arguments and then keyword arguments to be followed e.g.

calc(11866533567, b=18735)      #valid statement
#calc(a=11866533567, 18735)     #invalid statement as default argument is precedded before keyword

def nums(a,b,c,d,e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

nums(10,20,30,40,e=12)     #valid
# nums(10,b=33,34,45,e=19)   #invalid as default argument is passed in b/w keyword argument
# nums(a=10,20,30,40,12)     #invalid as default argument is passed in b/w keyword argument
#nums(10,20,30,40,b=12)     #invalid as multiple values are assigned for b i.e. 20 and 12 so PVM is going to throuw an error on screen

nums(10,b=20,c=30,d=40,e=12)  #valid positional arguments followd by default argumnets
nums(10,e=20,b=30,c=40,d=12)  #valid as keyowrd arguments order is not important




#Default Arguments : defined at the function defination, in case the user forget to pass the arguments default argument will be utilised for computation and no error will be thrown
                #default argument should be last argument (at defination/declaration) i.e. default argument has to be the last arguments.
                        # To be Noted - Exception : but we can take variable lenth arguments after default arguments
def greet_me(guest='Harry',mes="Good Morning"):
    print("Hello :", guest,mes)

greet_me()              #as no argument is passed default argument will take care
greet_me('Good Night')  #positional argument will take it over
greet_me(mes="Good Afternoon")   #keyword argument will take it over

#important note : same rule as mentioned above i.e. if in case you want to use both positional and keyword arguments then you must first pass positional arguments and then keyword arguments to be followed e.g.


#catering Point 3 : we can take variable lenth arguments after default arguments
def fun1(x='wwf',*my):
    print(x,my)

fun1('Ramyond','Radian','Relaxo')


#Variable Length Arguments :  variable number f arguments can be passed
    #after Variable length argument only keyword arguments are valid arguments
    #we are not allowed to take multiple variable lenth arguments
   #2 Types of Variable length arguments
    #args : become tuple
    #kwargs : become dictionary

#*Args : we are not bound to use only args it can be any other variable name :- it gives flexibility to user to pass variable
def nums(*args):
    print("The Lenth of tuple passed as argument is",len(args))
    for x in args:
        print("Argument is :",x)

nums(10,20)
nums(12,13,14)

#after default arguments ,we cannot take normal arguments but we can take variable lenggth arguments e.g.
def fun1(x='wwf',*my):
    print(x,my)

fun1('Ramyond','Radian','Relaxo')


# **kwargs :  passsed in key-value pairs  and kwargs will become dictionary


def mult_key_value(**kwargs):
    print(type(kwargs))
    print(kwargs)

mult_key_value(name='Ferrari',model='Spider')

    #we can utilise args and kwargs both togther
def mult_key_value(*args, **kwargs):
    print(type(kwargs))
    print("Arguments: ", args)
    print("Dict: ",kwargs)

mult_key_value(10,13,15,17,name='Ferrari',model='Spider')

    #NotE: After keyword arguments no oth type of arguments are allowed to pass uncomment the below code to get the error
# def mult_key_value(*args, **kwargs, x):
#     print(type(kwargs))
#     print("Arguments: ", args)
#     print("Dict: ",kwargs)
#
# mult_key_value(10,13,15,17,name='Ferrari',model='Spider',x=22)

