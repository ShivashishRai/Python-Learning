
# #Public Access mofifier
# class AccessModf:
#
#     def __init__(self):
#         self.name = "Shiv"
#         self.age = 32
#
# access = AccessModf()
# print(access.name)
#

#Private Access mofifier
class PrivateAccessModf:

    def __init__(self):
        self.__name = "Puju"    #__before variable name signifies private variable
        self.__age = 26

access = PrivateAccessModf()
#print(access.name)             #not be able to access as __name is private variable
print(access._PrivateAccessModf__name)         #_ClassName__variable to access the private variables defined in class
print(access._PrivateAccessModf__age)

print(access.__dir__())           # to get list of method can be executed on the class object



#Protected access modifier

class Student():

    #protected variables
    _name = None
    _classs = None
    _roll_no = None

    #constructor of super class
    def __init__(self, name, classs, roll_no):
        self._name = name
        self._classs = classs
        self._roll_no = roll_no
    #protected member function - can be accessed from class or derived class
    def _displdetails(self):
        print("Sudent Name:", self._name)

    #protected member function
    def _displroll(self):
        print("Student roll no", self._roll_no)

#derived class from student
class WeakStudent(Student):
    #constructor for derived class and calling the parent class constructor
    def __init__(self,name, classs, roll_no):
        Student.__init__(self, classs, name, roll_no)

    #public member function
    def studentinfo(self):
        print("Student classs is : ",self._classs)
        self._displdetails()
        self._displroll()

#creating object for derived class
weak = WeakStudent("Shiv", 9, 23)

#calling public member function of derived class
weak.studentinfo()
print(weak.__dir__())
