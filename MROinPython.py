

class A:
    def firstname(self):
        print("Shiv")

class B(A):
    def firstname(self):
        super().firstname()
        #print("Rai")

b = B()
b.firstname()
