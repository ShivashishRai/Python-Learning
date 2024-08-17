
#passing variable arguments to a function
#args
   # Are run time list of variable length

def sumof(*args):
    res = 0
    for x in args:
        res = res + x
    return (res)
sumoff = sumof(1,2,3,19,21,19)
print(sumoff)

#Example 2
#kwargs
  # passing dictionary as an argument to the function

def passingdict(**kwargs):
    print(kwargs["lstname"])

passingdict(fname="Shivashish",lstname = "Rai", Company="Fiserv",salary=10000)

#Example 3
print("The example of variable keyword or to better say dictionary arguments passed as argument in a function")
def mykwagsexample(**kwargs):
    for key,value in kwargs.items():
        print("%s = %s" %(key, value))


mykwagsexample(first = "Shivashish", middle = "Kumar",last = "Rai")



#Example 4: WAP to demonstrte the example of args and kwargs both in a single program:

def multarg(*args,**kwargs):

    print("args:",args)
    print("kwargs: ", kwargs)

multarg("shiv","ashish","rai",first="Neha", middle=" ",last="rai")








