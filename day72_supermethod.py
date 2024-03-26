
#super() method refer to parent class.
# when a class inherits from a parent class, it can override or extend the methods
# defined in parent class. However sometimes you might want to use the parent class methods
# in clild class


#Parent class
class Employee():
    #parent method
    def employee(self):
        # self.name = name
        # self.id = id
        # self.profile = profile
        print("You're working as an Employee: ")

#derived class
class Devloper(Employee):

    #dervied class method
    def dev(self):
        print("You're working as an dev enginner: ")
        super().employee()     #calling the method of the parent class from derived class method

#creating object for the derived class
devloper = Devloper()
devloper.dev()

