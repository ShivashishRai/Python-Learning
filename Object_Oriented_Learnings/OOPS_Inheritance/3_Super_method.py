
#super() method : super is build in method to call parent class constructo, methods, variables explicitly from child class.
        #useful in case when parent and child both classes contain method or variables with same name

class Parent():
    def method(self):
        print("Parent class method")


class Child(Parent):
    def method(self):
        super().method()          #parent class method will be called and executed
        print("Child class method")

child_obj = Child()
child_obj.method()


