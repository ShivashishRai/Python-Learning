
#Medhod inside Method is call as Nested Methods and it's applicable in python
   #When same operation is required to perform on multiple time inside the method so it's better to wrap the code in method inside the parent method
#Syntax
class Test:
    def mytest1(self):
        def mytest2():
            pass
test = Test()



#example 1 : Nested Methods :
class Test:
     def localmethod(self):                                  #Parent Method
         def sublocal(a,b,c):                                # defined Nested Method with argument
             print("Value of first argument passed to sub local method is:", a)
             print("Value of second argument passed to sub local method is:", b)
             print("Value of third argument passed to sub local method is:", c)
             print(' ')

         sublocal(11,12,13)                                #calling method with required argument
         sublocal(14,15,16)
         sublocal(17,18,19)

mytest = Test()                                           #creating object/reference  for the class
mytest.localmethod()                                      #calling the parent method which will trigger the nested method i.e. line 22 will call the nested method


