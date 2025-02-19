
#Decorator : is a function which can take a function as an argument and return enhanced function.
    # Please Note that Decorator functon take function as an input/argument and returns function as an output, So function not meeting both of these criteria cannot be catagorised as decorator



def decor(func):                        #decorator function take func as an argument

    def inner():                       #decorating the function with enhanced feature so that why defined another function
        print(" I am here to beautify non glamrous function ")
        func()
    return inner                       # inner function is executed and returned

@decor                  #calling the function (act as decorator)
def func():
    print("I am non glamrous function")

func()


# Example 2 : Decorator with arguments

def decor_of_add(ADD):

    def main_deco(x,y):
        print("I am going to decor the normal add function:")
        print("The sum of two number is {} and {}".format(x,y))
        ADD(x,y)
    return main_deco

@decor_of_add
def add(a,b):
    print(a+b)

add(10,15)
add(200,178)


#Example 3 : Decoratoring function based on certain condition only


def decor_disp_name(func):
    def name_inner_func(name):
        if name == "Krishna":
            print('*' * 25)
            print("I am lord Krishna residing in Vrindavan")
            print('*' * 25)

        else:
            func(name)
    return name_inner_func

@decor_disp_name
def disp_name(name):
    print("My Name is ", name)

disp_name("Rama")
disp_name("Krishna")
disp_name("Laxman")

















