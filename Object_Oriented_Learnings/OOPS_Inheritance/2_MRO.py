
#Method Resolution Order
        #The process of deciding method for the given method call is called as MRO


class A:
    def method_a(self):
        print("Method A")
class B:
    def method_a(self):
        print("Method B")
class C:
    def method_a(self):
        print("Method C")
class D(A,B):
    def method_a(self):
        print("Method D")
class E(B,C):
    def method_a(self):
        print("Method E")
class F(D,E,C):
    def method_a(self):
        print("Method F")


print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
print(E.mro())
print(F.mro())



#MRO - Alogorithm :
