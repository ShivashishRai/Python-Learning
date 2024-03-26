
class Employee:

    def __init__(self,name,company):
        self.name = name
        self.company = company

    def show_details(self):
        print(f"Name: {self.name} and works at : {self.company} ")

class Programmer(Employee):
    def language(self):
        print("Sxy")

emp = Employee("Shivas","Fiserv")
emp.show_details()

prog = Programmer("Puju","kotak")
prog.show_details()

prog.language()
