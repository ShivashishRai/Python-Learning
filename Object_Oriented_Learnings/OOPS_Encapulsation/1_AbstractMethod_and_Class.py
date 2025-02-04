
#Abstract Method and Abstract Class

#Abstract : which is not complete (just giving basic idea or skelton )
    #Abstract Method : has only declaration but not body , method which is not completeness
        #in future , under the child classes these methods are required to be implement.
        #Advantage of abstract method : by declaring abstract method in parent class, we can provide guidelines to the child classes, such that which method child has to implement


from abc import abstractmethod                    #import abstract method from abc module
class Vehicle:

    @abstractmethod                               #use the decorator to define method as abstract method (i.e only defination is defined not actua implemantation) child class will take care of its implemantation
    def noofwheels(self):
        pass


#Abstract Class : implemantation of class which is not complete such partially implemanted classes are called Abstract class.
    #Every abstract class in python is the child class of ABC: (Abstract Base Class) class present in abc module.
    


