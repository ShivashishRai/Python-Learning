
#Variables : Local and Global Variables and their scope

# Local Variables: scope is limited to the deifined inside function/method only
#Gloabl Variables: scope is throught the program


a= 10    # scope is global i.e. accessiable through the program

def my_local():
    b = "Atto 3"   #scope is local to my_local function only
    print(b)
    print(a)

my_local()
#print(b)    #Uncommenting this line will lead to an error as variable b scope was only limited to my_local function



# Global variable : to make global variable available to the function so that we can perform required modification
                # to declare global variables inside functions

a=10           #global variable :available throughout
def fun1():
    a=999      #local variable
    print("Fun1 ",a)

def fun2():
    print("Fun2:", a)

fun1()    #a = value entered by user
fun2()    #a = 10 globally defined

#to overcome above limitation i.e if we wish to change a value inside the fun1 then we need to define a as global variable inside the fun1 i.e.

a=10           #global variable :available throughout
def fun1():
    global a
    a=999      #local variable
    print("Fun1 ",a)

def fun2():
    print("Fun2:", a)

fun1()    #a = value entered by user
fun2()    #a = value will be over powered by fun1 value