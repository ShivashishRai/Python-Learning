

def myfunc(*args):
    for x in args:
        print(x)

myfunc('maruti','suzuki')


# def myfunckw(**kwargs):
#     for x,y in kwargs.items():
#         print("%s == %s" %(x,y))
#
# myfunckw(car:"maruti",brand:"suzuki")

def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))

# Driver code
myFun(first='Geeks', mid='for', last='Geeks')



#WAP to demonstarte usage of args and kwargs into the same function

def newparams(*args,**kwargs):
    for arg in args:
        print("Args arguments:", arg)

    for key,value in kwargs.items():
        print("Kwargs Arguments: %s ==%s" %(key,value))

newparams('shivas','rai','kumar',salary=25000, profession = "Testing IT Software")



