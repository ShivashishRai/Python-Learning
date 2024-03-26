
#dir() method returns list of all the attrubutes and methods available for an object

name = "Shivas"

print(dir(name))
#print((name.swapcase()))


# __dict__ returns a dictionary representation of an objects attributes

class Person:
    def __init__(self, hobby, passion):
        self.hobby = hobby
        self.passion = passion

person = Person("Sports", "Lawn Tennis")
print(person.__dict__)


#help() method used to get help documentation for an object, including the description of its attributes and methods
print(help(Person))

