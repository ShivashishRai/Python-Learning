
#Public Member : by default every variable or method are Accessiable across inside of class or outside of the class


class Test:

    def __init__(self):
        print("Control is in Construcor and will be called once you create Object for the class")
        self.x = 10            #public variable

    def m1(self):              #public method
        print("Method 1 in Test class")

    def m2(self):              #public method
        print("Method 2 in Test ")
        print(self.x)
        self.m1()

test_obj = Test()
test_obj.m2()


# Private : method or variable is defined as private then we can access that member only within the class and accessing member outside of the class is restricted.
        # to denote method or variable as private :    self.__x = 10    -> (private variable)         and       def __m1(self):    -> (private method)


class Test:

    def __init__(self):
        print("Control is in Construcor and will be called once you create Object for the class")
        self.__x = 10            #private variable

    def __m1(self):              #private method
        print("Method 1 in Test class is defined as Private method")

    def m2(self):              #public method
        print("Method 2 in Test ")
        print(self.__x)         #private variable will be accessiable as we are trying to access within class
        self.__m1()              #private class will be accessiable as we are trying to access within class

test_obj = Test()
test_obj.m2()

# test_obj.__m1()    # un commenting will throw an error as mentioned private method/ variable is not accessiable outside class



#Name Manglling :  we can access private memebre (method or variable) by calling    Syntax --> {  ClassReferenceObject._ClassName__privatemembername  }
        # it compromise with the security in python
class Test:

    def __init__(self):
        print("Control is in Construcor and will be called once you create Object for the class")
        self.__x = 10            #private variable

    def __m1(self):              #private method
        print("Method 1 in Test class is defined as Private method")

    def m2(self):              #public method
        print("Method 2 in Test ")
        print(self.__x)         #private variable will be accessiable as we are trying to access within class
        self.__m1()              #private class will be accessiable as we are trying to access within class

test_obj = Test()
print(test_obj.__dict__)
print(test_obj._Test__x)            #ClassReferenceObject._ClassName__privatevariablename
test_obj._Test__m1()                #ClassReferenceObject._ClassName__privatemethodname

# test_obj.__m1()
