
#Interface : An Abstract Class containing only Abstract Methods is known as Interface ( only  acts as Simple Requirement Specification )
# We can handle interface requirement by using abstract method and abstract class concept
# Direct interface concept is not available in python

from abc import ABC,abstractmethod
class ICC(ABC):           #as this class consists of only abstract method so we can call this as an Interface

    @abstractmethod
    def bcci(self):            #abstract method which only consists of defination and child class will take care of it's actual implemantation
        pass

    @abstractmethod
    def bcb(self):
        pass

    @abstractmethod
    def pcb(self):
        pass

    @abstractmethod
    def ecb(self):
        pass


class Mens_Cricket_Boards(ICC):                                  #Abstract Class are is consist of partial implemantation of abstract methods i.e. ECB is not deen defined
    def bcci(self):
        print("Welcome to indian cricket board")
    def pcb(self):
        print("Welcome to Pakistan cricket board")

    def bcb(self):
        print("Welcome to Bangladesh cricket board")


class Women_Cricket_Board():                                    #Concrete Method as this contain ECB method which completes the methods defined under instance method
    def bcci(self):
        print("Welcome to women indian cricket board")
    def pcb(self):
        print("Welcome to women Pakistan cricket board")

    def ecb(self):
        print("Welcome to England and Whales cricket board")


mens_boards_obj = Mens_Cricket_Boards()             #This line will throw an error in case you comment line 42, 43 as without implemantation of all methods defined in interface we wot be able to create ab object for class
mens_boards_obj.bcci()

# women_boards_obj = Women_Cricket_Board()
# women_boards_obj.pcb()


#Basic Difference b/w Interface ,  Abstract Class and Concrete Class

'''
In case we just know about requirement specification and no idea about implemantation then we opt for Interface.
In case we know about Implemantation (Partially only) then we opt for Abstract Class. 
In case are complete implementation and its ready for service then we opt for Concrete class.
'''

