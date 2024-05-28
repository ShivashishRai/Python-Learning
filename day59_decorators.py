
def name_decor(name):
    def enchance_name():
        print("action need to be performed before decorating name function")
        name()
        #print("after decorating name function")
    return enchance_name

@name_decor
def name():
    print("My Name is : Shiv")

#Long way to call decorator without @
# decoration = name_decor(name)
# print(decoration())

#shorter was use @decorating function name i.e @name_decor
name()

print("**************************************************************")
def addi(number):
    def summ():
        first_num=number()
        result = first_num+12
        return result
    return summ

@addi
def number():
    return 19

print(number())


