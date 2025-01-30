
#Types of Variables
        # instance variable - value of variable varied from object to object and for every object seprate copy will be created
                    # in general instance variables are defined inside constructor by using self

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

        # #static variables/class variable
            # value of variable not varied from object to object then static variables are best recommented to use

class Student:
    school_name = 'Kendriya Vidayalaya'           #static Variable
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

        #local variables : Variable defined in methods for local use i.e. self are local variables
class Student:
    school_name = 'Kendriya Vidayalaya'           #static Variable
    def __init__(self,name,sub,marks):                 #constructor will be automatically triggered once object is created
        self.name = name             #instance-variables
        self.sub = sub               #instance-variables
        self.marks = marks           #instance-variables

    def exams(self):                      #method
        x = 10                       #local variable
        for i in range(x):           #x - local variable
            print(i)
        print("Name of Student: ",self.name)      #using instance variables
        print("Subject is : ",self.sub)

stud1 = Student('Neha','Hindi',77)   #Reference Variable/Object is created and constructor will automatically trigger
stud1.exams()                        #exams method will be triggered
print(stud1.marks)



