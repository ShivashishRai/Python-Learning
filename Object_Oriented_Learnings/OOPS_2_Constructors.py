
#Constructors : is special method which automatically injects once object for the class is created
    # name of constructor is always __init__()
    #self is the first parameter passed which contain the reference of the current object
    #per object constructor will be executated only once
    # main purpose is to declare and initialize instance variables
    #there must be atleast one argument (i.e. self) passed with constructor else we will end up getting error
    #Constructor are optional in python class. if we are not providing constructor default constructor will be provided by PVM
    #We can call constructor explicitly, then it will be executed just like normal method and new object won't be created
    # In case user define multiple constructor then, PVM will consider only last constructor defined ( No Error we will be getting for defining constructor) i.e constructor overloading not possible
class Automobile:
    def __init__(self):
        print("I am constructor and will be called automatically once you crate object for class Automobile")

auto = Automobile()



#Constructor are optional in python class. if we are not providing constructor default constructor will be provided by PVM
class Automobile:
    def colour(self):
        print("I am method without constructor")

auto = Automobile()
auto.colour()          #is gonaa be valid statement as default constructor will be executated by PVM

    #iMPORTANT TO nOTE: Without constructor our object will be blank without data so it's best recommended to have constructor


# We can call constructor explicitly, then it will be executed just like normal method and new object won't be created
class Automobile:
    def __init__(self):
        print("I am constructor")

auto = Automobile()          #first time constructor is call automatically
auto.__init__()              #explicit call to constructor
auto.__init__()
auto.__init__()


# In case user define multiple constructor then, PVM will consider only last constructor defined ( No Error we will be getting for defining constructor)

class Automobile:
    def __init__(self):                                  #this will no longer be applicable as last defined constructor will hold it's ground and this will be available for garbage collection
        print("I am constructor")

    def __init__(self, name):
        self.name = name
        print("I am constructor 2 :", self.name)

# auto = Automobile()             #this will throw an error on screen as last constructor defined required one argument
auto = Automobile('Porche')



# Program to demonstrate object

class Test_Cricket:
    def __init__(self,days):
        self.days = days

class One_Day_Cricket:
    def __init__(self, days):
        self.days = days

test = Test_Cricket(5)
one = One_Day_Cricket(1)
test.__init__(6)
one.__init__(2)


#It's possible to declare a method with same class name
class Test_Cricket:
    def Test_Cricket(self):           # closely observ with intention i kepy method name same as class name
        print("Test is Best")

test = Test_Cricket()    #__init__() will be executated (PVM will inject constructor as we create object) / reference variable is created
test.Test_Cricket()      #method will be execuated



