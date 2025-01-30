
#Static Variables : TO BE USED only When value of the variable is not varied from one object to another object
    #only one copy will bre created


    #Various places to define static variables
        #generally defined within class but outside of any methods
class Student:
    school_name = 'Kendriya Vidayalaya'           #static Variable

    def sports(self,mysports):
        self.mysports = mysports

print(Student.__dict__)

         #Inside constructor and instance method by using class name

class Test:
    x = 50

    def __init__(self):
        Test.y = 20                             #static variable is defined by the class name i.e. Test.y

    def my_test_method(self):
        Test.z = 30                             #static variable is defined by the class name i.e. Test.z

t1 = Test()                                     #Object will be created for Test class and default constructor will also be injected i.e. instance variables will be created
t1.my_test_method()                             # this will create memory allocation for z in object
print(Test.__dict__)                            #


        #inside class method by using either class name or cls variable (class object variable)
class Test:
    x = 50

    def __init__(self):
        Test.y = 40                             #static variable is defined by the class name i.e. Test.y

    @classmethod
    def my_test_method(cls):
        Test.z = 50                             #static variable is defined by the class name i.e. Test.z
        cls.i=60                                #static variable is created using cls object

t1 = Test()                                     #Object will be created for Test class and default constructor will also be injected i.e. instance variables will be created
t1.my_test_method()                             # this will create memory allocation for z and i in object
print(Test.__dict__)


        # inside static method by using class name i.e. classname.variablename
class Test:
    x = 70

    def __init__(self):
        Test.y = 80  # static variable is defined by the class name i.e. Test.y

    @staticmethod
    def my_test_method():
        Test.j = 90  # static variable is defined by the class name i.e. Test.z



t1 = Test()  # Object will be created for Test class and default constructor will also be injected i.e. instance variables will be created
t1.my_test_method()  # this will create memory allocation for z and i in object
print(Test.__dict__)

        # Outside class method by using either class name

class Test:
    e = 70

    def __init__(self):
        Test.f = 80  # static variable is defined by the class name i.e. Test.y

    @staticmethod
    def my_test_method():
        Test.g = 90  # static variable is defined by the class name i.e. Test.z



t1 = Test()  # Object will be created for Test class and default constructor will also be injected i.e. instance variables will be created
t1.my_test_method()  # this will create memory allocation for z and i in object
Test.h = 100         #static variable defined outside the class using class_name.variablename
print(Test.__dict__)



    #How to modify(update) value of static variables
        #We can update values of static variables either by classname or cls variables
        # We cannot use self or object reference to update static variables

class Test:
    a = 10

    @classmethod
    def m1(cls):
        cls.a=20

    @staticmethod
    def m2():
        Test.a=30

t1 = Test()
t1.m1()
t1.m2()

print(Test.a)


        #How to delete Static Variables of a class:
            #Anywhere : del classname.variablename
            #classmethod : del cls.variablename

class Automobile:
    company = 'Maruti'                  #static variable

    @classmethod
    def details(cls):
        #del cls.company                 #to delete static variable inside classmethod we have used cls.variablename
        del Automobile.company           #to delete static variable inside classmethod we have used Classname.variablename "uncomment above line to delete by class object"

print(Automobile.__dict__)              #dictionary of class
Automobile.details()                    #to execute the method (this will delete the static variable )
print(Automobile.__dict__)

            #Another example of delete static variable

class TestStatic:
    i = 10          #static variable
    mi = 11         #static variable
    def __init__(self):
        TestStatic.j = 12         #defined staic variable inside teh constructor
        del TestStatic.i

    @classmethod
    def myclass(cls):
        TestStatic.k=13           # static variable inside class method (i.e. cls.staticvariablename) is also valid syntax
        del cls.mi               #delete static variable inside class method by classname.staticvariablename or cls.staticvariablename

    @staticmethod
    def mystatic():
        TestStatic.l =14
        del TestStatic.k

    def genmethod(a,b):
        TestStatic.m=15
        del TestStatic.l
        return a+b


print(TestStatic.__dict__)           #static metohd will be  i - 10 and mi - 11
test_obj = TestStatic()
print(TestStatic.__dict__)          # static method - mi - 11 and j  - 12
test_obj.myclass()
print(TestStatic.__dict__)          # static method - j -12  and k - 13
test_obj.mystatic()
print(TestStatic.__dict__)          # static method - j -12  and l - 14

gen = TestStatic.genmethod(12,15)   # static method - j -12  and m- 15
print(TestStatic.__dict__)
TestStatic.n = 16                   # new static metod will be intialised n - 16
print(TestStatic.__dict__)          # static method - j -12  and m- 15 and n - 16

del test_obj.j                      # as mentioned we cannot delete static variable by class object/reference variable so we will end up getting an Attribute error