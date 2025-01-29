
#OOP - Realtime entities called objects

#Important things to known - Class , Object and Reference Variables
  #class -  acts as a blue print /plan/model design for objects
  #Object - Physical existance of a class
  #Reference Variable - used to refer objects, using refenece variable we invoke functionality of object

#syntax
class Student:
    def __init__(self):                 #constructor will be automatically triggered once object is created
        self.name = 'Sikha'             #instance-variables
        self.sub = 'Compt'
        self.marks = 39

    def exams(self):                      #method
        print("Name of Student: ",self.name)      #using instance variables
        print("Subject is : ",self.sub)


stud = Student()              #Reference Variable/Object is created and constructor will automatically trigger
stud.exams()                  #exams method will be triggered
print(stud.marks)

#Types of Variable
#1. Instance(Object)                        2. Static Variables (Class)                     3. Local Variables(Method)

#Types of Methods
#1. Instance Method                         2 Class Method                                  3. Static Method



# Program to demonstrate example of self and reference variable significance
class Student:
    def __init__(self,name,sub,marks):                 #constructor will be automatically triggered once object is created
        self.name = name             #instance-variables
        self.sub = sub
        self.marks = marks

    def exams(self):                      #method
        print("Name of Student: ",self.name)      #using instance variables
        print("Subject is : ",self.sub)

stud1 = Student('Neha','Hindi',77)              #Reference Variable/Object is created and constructor will automatically trigger
stud1.exams()                  #exams method will be triggered
print(stud1.marks)

stud2 = Student('Mehul','English',88)              #Reference Variable/Object is created and constructor will automatically trigger
stud2.exams()                  #exams method will be triggered
print(stud2.marks)


#Important Point to note regarding - Self : Self is reference variable which points to current object, to access current object we can use self
      # First argument to constructor is always self
            #First argument to instance method is always self
      # User not required to prvide value to self variable, PVM itself provide value
      # Use self within class only
        #inside constructor we can use self to declare object related variables(instance variables)
        #inside instance variables we can use self to access values of instance variables

      # self is not a keyword : but it's best recommended to use self






