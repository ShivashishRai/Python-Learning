
x = 'Ishu'

def myname():
    name = "Apra"
    print(name)
    global x       #defining the global variable
    x = "Ashu"
    #print(x)

myname()
print(f"Outside the funcation value of {x} ")



#Example 2

x =10
def my_fumction():
    global x
    x =4
    y=5

    print(y)

my_fumction()
print(x)

#Example 3 :

x = 'Ashish'
print("I am the name defined putside function",x)
def myname():
    x = "Apra"
    print("I am the name local:",x)
    # global x       #defining the global variable
    # x = "Ashu"
    #print(x)

myname()
print(f"Outside the funcation value of {x} ")


