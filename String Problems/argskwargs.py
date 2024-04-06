

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
