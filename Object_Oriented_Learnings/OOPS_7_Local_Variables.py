
#Local Variables
    #We can define variables inside method directly
    #local variable will be created at time of method execution and will be destroyed once method execution is complete
    #local variables cannot be accessed outside of the method

class Localvariabledemo:

    def test1(self):
        a=101               #local varibale defined for test1 method
        print(a)

    def test2(self):
        b=102               #local variable for test2 method
        #print(a)             #this will lead to an error as scope of local variable is within the defined method only
        print(b)

test = Localvariabledemo()
test.test1()
test.test2()