
#Passing members of one class to another class
    #We can access members (variables and methods) of one class inside another class

class Employee:
    def __init__(self,empname, empno, empsal):
        self.empname= empname
        self.empno = empno
        self.empsal = empsal

    def display_employee(self):
        print("The naem of employee is: ", self.empname)
        print("The emp no of employee is: ", self.empno)
        print("The emp no of employee is: ", self.empsal)


class  Manager():
    def sal_update(sal):
        sal.empsal = sal.empsal +100000
        sal.display_employee()

e = Employee("Shriniwash",883678,68400)          #created object and reference variable for Employee
Manager.sal_update(e)                            #sal will be created as reference variable for Manager ( "Shriniwash",883678,68400)
