
#OOP - Realtime entities called objects

#Important things to known - Class , Object and Reference Variables
  #class -  acts as a blue print /plan/model design for objects
  #Object - Physical existance of a class
  #Reference Variable - used to refer objects, using refenece variable we invoke functionality of object

#syntax
class Student:
    def __init__(self):                 #constructor
        self.name = 'Sikha'             #variables
        self.sub = 'Compt'
        self.marks = 39

    def exams(self):                      #method
        print("Name of Student: ",self.name)
        print("Subject is : ",self.sub)


stud = Student()              #Reference Variable/Object is created
stud.exams()
print(stud.marks)

#Types of Variable
#1. Instance(Object)                        2. Static Variables (Class)                     3. Local Variables(Method)

#Types of Methods
#1. Instance Method                         2 Class Method                                  3. Static Method