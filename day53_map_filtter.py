
#MAP
#Applies to a function to each element in a sequence and reduce a new sequence containing the transfered elemnts

def cube(x):
    return x*x*x

my_list = [12,14,17,19,23,11,9]
mapslist = list(map(cube,my_list))
print(mapslist)

#Filter

def filter_fun(x):
    if x%2!=0:
        return x

list_filter = list(filter(filter_fun,my_list))

print(list_filter)
