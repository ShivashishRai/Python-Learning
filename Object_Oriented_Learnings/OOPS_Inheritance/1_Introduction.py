
#Inheritance : Inheriting properties from one class to another is known as inheritance

#Types of Inheritance
#    Single    Multi-Level   Multiple       Hierarichical

#Single Inheritance

class Myparent:
    def parent_mthod(self):
        print("Parent method")

class Mychild(Myparent):             #MyChild is inheriting the properties (i.e methods and variables) of Myparent class
    def child_method(self):
        print("Child Method ")

mychild = Mychild()
mychild.child_method()
mychild.parent_mthod()

#Multi-Level Inheritance : Multiple Level of Inheritance, inheriting members from multiple parent classes to a single child class
class Myparent:
    def parent_mthod(self):
        print("Parent method in Multi Level Inheritance")

class Mychild(Myparent):             #MyChild is inheriting the properties (i.e methods and variables) of Myparent class
    def child_method(self):
        print("Child Method in Multi Level Inheritance ")


class Mychild_2(Mychild):
    def child_method_2(self):
        print("Child Method 2 in Multi Level Inheritance")

mychild = Mychild_2()
mychild.child_method_2()
mychild.child_method()
mychild.parent_mthod()


#hIRERCHICAL iNHERITANCE : One Parent have Multiple child

class Myparent:
    def parent_mthod(self):
        print("Parent method in Hierarichical Inheritance")

class Mychild(Myparent):             #MyChild is inheriting the properties (i.e methods and variables) of Myparent class
    def child_method_1(self):
        print("Child Method in Hierarichical Inheritance ")


class Mychild_2(Myparent):
    def child_method_2(self):
        print("Child Method 2 in Hierarichical Inheritance")

mychild = Mychild_2()
mychild.child_method_2()         #valid
mychild.parent_mthod()           # valid

#mychild.child_method()           #invalid as mychild is not having  access to MyChild class properties and methods


# Multiple Inheritance : Multiple Parent class and Single child class *Exclusive feature of Python*
class Myparent:
    def parent_mthod(self):
        print("Parent method in Multiple Inheritance")

class Mychild():             
    def child_method(self):
        print("Child Method in Multiple Inheritance ")


class Mychild_2(Myparent,Mychild):         #inheriting two parent classes (multiple inheritance)
    def child_method(self):
        print("Child Method 2 in Multiple Inheritance")

mychild = Mychild_2()         #creating object/ reference variable for MyChild class which will have access to all inheriated child classes
mychild.child_method()                      #child method of own class will get first priority in and in case it's not in the parent class (one resposible for creating object) then preference will be allocated as per class priority defined in step 75
mychild.parent_mthod()                      #parent will execute as child object class parent is inherating the parent
mychild.child_method()


#Hybrid Inheritance :Combination of two or more of the obove mentioned inheritance

class Parent:
    def m1(self):
        print("Parent Method")
class child1(Parent):           #Hirechical
    def m1(self):
        print("child 1 Method")
class child_2(Parent):           #hirechichal
    def m1(self):
        print("child 2 Method")
class sub_child(child1,child_2):    #Multiple inharitance  (i.e.   Hybrid Inharitance as it consist of hyrichical and multi inhritance)
    def m1(self):
        print("sub child Method")


obj_sub_child = sub_child()
print(sub_child.mro())
#obj_sub_child.m1()                #first sub_child class method will be called
#obj_sub_child.m1()                #Child_2 m1 method will be called in case it's not found in sub_child class ( un-comment 95-96 line)
obj_sub_child.m1()                 #Child_1 m1 method will be called in case it's not found in child_2 class ( un-comment 95-96, 92-92 line)


''' Note : In case no class contain the method then it will first check the class object and in case that also dosn't contain the method so we will end 
        --up getting  an attribute error on screen. 
        
        - Object is the python inbuilt class. 
        - Every class in python is an child class of object class directly or indirectly 
        - in case our class in not child of any class then it is direct child of object class. '''



        

