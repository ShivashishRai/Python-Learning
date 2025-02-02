
class Person:
    #Class variable
    name="Shivashish"
    occupation="IT Enginner"
    salary= 170000

    def myfunc(self):
        print(f"My name is {self.name}, I work as {self.occupation} with a salary package of {self.salary}")

person_obj = Person()
# person_obj.myfunc()

person_obj.name = "Ishu"
person_obj.occupation = "Student"
person_obj.salary="N/A"

person_obj.myfunc()