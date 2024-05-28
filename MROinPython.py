

class A:
    def firstname(self):
        print("Shiv")

class B(A):
    def firstname(self):
        pass
        super(B,self).firstname()
        #print("Rai")

b = B()
b.firstname()
