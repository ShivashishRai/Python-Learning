
#Instance Methods
    #at least one instance variable
    # first argument for instance method is always self
    # within class we can call instance method by self whereas outside


#Program to demonstrate example of instance method and variable
class Student:

    def __init__(self,name,marks):             #constructor
        self.name = name                       #instance method
        self.marks = marks

    def display(self):                          #instance method
        print("Hello ", self.name)
        print("Your Scored :",self.marks)
        self.grades()                           #we can call instance method by self.method name

    def grades(self):                             #instance method
        if self.marks >= 75:                      #istance variable
            print("You are passed with Grade A")
        elif self.marks >= 60:
            print("You are passed with Grade B")
        elif self.marks >=45:
            print("You are passed with Grade C")
        else:
            print("Sorry {} to say that you didn't clear the exam".format(self.name))

student_num = int(input("Enter no. of student: "))
for x in range(student_num):
    name = input("Enter Student Name")
    marks = int(input("Enter student marks :"))
    stud = Student(name,marks)                       #object reference for student class is created which will trigger constructor and instance variable will be allocated into the object
    stud.display()                                  #outside the class we can call instance method by classreferenceobject.methodname

#stud.grades()


#Getter and Setter methods : when we don't know the data at the beigning AND LATER WE WANT TO PERFORM INITIALISATION then we it's best to use getter and setter method
    # we are not allowed to pass more than one variable in setter method
class Student:

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks

stud_get_set=Student()            # this is creating dummy object
name = input("Enter Student name: ")
marks = int(input("Enter Student Marks: "))

stud_get_set.setName(name)        #name is initialsed here
stud_get_set.setMarks(marks)      #marks is initalised here

my_stud_name = stud_get_set.getName()
my_stud_marks = stud_get_set.getMarks()
print("Student name fetced by getter method is :",my_stud_name)
print("Student marks fetced by getter method is :",my_stud_marks)




    #Class Method : In case we use static variables and no instance variables is used
        #cls is the first argument passed inside the class method which point to class object

class Student:
    collg = 'KALINGA'

    @classmethod
    def mycollg(cls):
        print("My Colleage name is: ",cls.collg)

Student.mycollg()             #calling class method


# WAP to count the number of object created for class

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count = MyClass.count +1

    @classmethod
    def mycountofclass(cls):
        print("Objects created for the class is: ", cls.count)

mycls1 = MyClass()
mycls2 = MyClass()
MyClass.mycountofclass()