
'''
classvariables are shared among all instances of the class defined outside of methods
'''

class Empl:

    company_name = "Maruti"

    def __init__(self, dept):
        self.dept = dept

    def departement(self):
        print(f"Company Name: {self.company_name},Department: ", self.dept)

emp = Empl('HR')
emp.departement()



