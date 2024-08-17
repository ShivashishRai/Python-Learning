
print("*************************************************")

def name_decor(myname):
    def beautify():
        print("I am here to beutify the name function")
        myname()
    return beautify

@name_decor
def myname():
    print("My name is Pooja kumari")

myname()

print("***************************** Decorators with Params ***************************")

def my_div_decor(divide):
    def div(x,y):
        print(f"I am going to {x} with {y}")
        if y ==0:
            print("Woooh you need to enter higher denominator")
            return
        else:
            return divide(x,y)
    return div


@my_div_decor
def divide(x,y):
    print(x/y)

divide(38,4)
divide(38,0)