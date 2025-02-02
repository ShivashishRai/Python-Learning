class Person:

    def __init__(self,name,occ):
       # Instance Variables
        self.name = name
        self.occ = occ

    def information(self):
        print(f"{self.name} is {self.occ}")

a = Person("shivas","IT")
a.information()

b = Person("Ishu", "Student")
b.information()

# class Person:
#
#   def __init__(self, name, occ):
#     print("Hey I am a person")
#     self.name = name
#     self.occ = occ
#
#   def info(self):
#     print(f"{self.name} is a {self.occ}")
#
#
# a = Person("Harry", "Developer")
# #b = Person("Divya", "HR")
# a.info()
#b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()

# b= Person('Ishu','Student')
# b.information()


# class Dog:
#     # Class Variable
#     animal = 'dog'
#     # The init method or constructor
#     def __init__(self, breed):
#
#         # Instance Variable
#         self.breed = breed
#
#     # Adds an instance variable
#     def setColor(self, color):
#         self.color = color
#
#     # Retrieves instance variable
#     def getColor(self):
#         return self.color
#
#
# # Driver Code
# Rodger = Dog("pug")
# Rodger.setColor("brown")
# print(Rodger.getColor())