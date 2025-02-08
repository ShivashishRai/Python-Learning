#
#
# #Function_Aliasing : giving name to function
#
# def fun1():
#     print("Function 1 ")
#
# myfun1=fun1     #Function Aliasing fun1 and myfun1 are function reference name object pointing to same function,  { fun1 and myfun1 pointing to same function object function alisaing}
# myfun1()        # this will call fun1() method as myfun1 is also pointing to same method as fun1 pointing to
#
#
# # Nested Function : Function inside another function is called as Nested function
#
# def outer():
#
#     print("Outer Method: ")
#
#     def inner():
#         print("Inner Method: ")
#
#     inner()                      #outer method going to call the inner method
#     print("Outer method completed Successfully")
#
# outer()
# #inner()    #Name error as scope of inner method is inside the outer method only

# Extend new functionality
    # 'Function can return another function'


def outer():

    print("Outer Method: ")
    def inner():
        print("Inner Method: ")
    print("Outer method completed Successfully")
    return inner                  # function is returned , keep in mind () is not included at the end of the method name if we define as inner() then this will be trigger inner() method which has bydefault None return type and it will be passed to myinner function object

myinner = outer()                # myinner will be reference object for inner function mentioend under outer function
myinner()


#Important Conclsion :
'''
*In python everything is treated as object even function also
*Every functoin is treated as object
*for existing function we can give another name (Function aliasing)
*Inside function, we can define another function(nested function)
* A function can return another function.
*We can pass a function as argument to another function

* f1=outter   #significes f1 and outter are pointing to the same function object. (Function Aliasing )
        whereas   f1 = outter()  # significes that outter function is executed and return value is assigned to f1 

'''