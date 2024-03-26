
def myfunc(x ,y ,z):
    if z == True:
        return x

    else:
        return y


results = myfunc(True,False,True)
print(results)


def myfunc(*args):
    even = []
    for i in args:
        if (i% 2) == 0:
            even.append(i)
        else:
            pass

    return even
even_list = myfunc(11, 14, 19,226, 119, 225, 471)
print(even_list)


def myfunc(string):
    new_st = []
    leng = len(string)
    for index in range(leng):
        if index % 2 == 0:
            new_st.append(string[index].upper())

        else:
            new_st.append(string[index].lower())

    return new_st
upper_lower = myfunc("SHIashishRaoiSCooLboUy")
print(upper_lower)




def myfunc(string):
    new_st = ''
    leng = len(string)
    for index in range(leng):
        if index % 2 == 0:
            new_st = new_st+string[index].upper()

        else:
            new_st = new_st+string[index].lower()

    return new_st
upper_lower = myfunc("SHIashishRaoiSCooLboUy")
print(upper_lower)

