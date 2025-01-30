
#Methods : 1. Instance Methods     2. Class Methods     3. Static Methods

    #Instance Methods : Methods containing even a single instance variables it dosn't matter presennce of static/local variables
        #self is the first argument which points to current object
        # no decorators are required


class Student:
    school_name = 'Kendriya Vidayalaya'           #static Variable
    def __init__(self,name,sub,marks):                 #constructor will be automatically triggered once object is created
        self.name = name             #instance-variables
        self.sub = sub               #instance-variables
        self.marks = marks           #instance-variables

    def exams(self):                      #Instance method as it contain instance varible
        stud_clas = 11                   #static variable
        print("Name of Student: ",self.name)      #using instance variables
        print("Subject is : ",self.sub)


    #Class Method : Method containing at least one class/static variable, dosn't matter the presence of local variables
        #cls is the first argument passed to the class method; class object will be created by PVM only once for each cass
        #@classmethod is used as a decorator

class Student:
    school_name = 'Kendriya Vidayalaya'           #static Variable
    def __init__(self,name,sub,marks):                 #constructor will be automatically triggered once object is created
        self.name = name             #instance-variables
        self.sub = sub               #instance-variables
        self.marks = marks           #instance-variables

    @classmethod                         #decorator to specifically define it's class method
    def exams(cls):                      #Class method as it contain class/static varible
        print("Student Study in :",cls.school_name)

#stud = Student('Supriya','CA',76)
Student.exams()                          #class name.class method






    # Static Method : Method containing no instance variable nor containing any static/class variable are static method
        # @staticmethod is used as a decorator

class Student:
    school_name = 'Kendriya Vidayalaya'           #static Variable
    def __init__(self,name,sub,marks):                 #constructor will be automatically triggered once object is created
        self.name = name             #instance-variables
        self.sub = sub               #instance-variables
        self.marks = marks           #instance-variables

    @staticmethod                         #decorator to specifically define it's static method
    def percentage(a,b,c):                      #static method as it dosnt contain eiter instance or class/static varible
        perc = (a+b+c)/300*100
        return perc

stud=Student('Ishu','English',64)
per = stud.percentage(74,82,87)         #to call static method classname.staticmethodname or objectreferencevariable.staticmethodname
print(per)
