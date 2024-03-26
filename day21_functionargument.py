
#passing argument to a function

#args
   # Are run time list of variable length

#res=0
def sumof(*args):
    res = 0
    for x in args:
        res = res + x
    return (res)
sumoff = sumof(1,2,3,19,21,19)
print(sumoff)

#kwargs
  # passing dictionary as an argument to the function

def passingdict(**kwargs):
    print(kwargs["lstname"])

passingdict(fname="Shivashish",lstname = "Rai", Company="Fiserv",salary=10000)


