

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(10))



def myfunc(n):
  return lambda a : a ** n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(f"Square of the number",mydoubler(10))
print(f"Cude of the number",mytripler(10))


my_list = [11,13,99,32,19]
filter_final = list(filter(lambda x : (x%2==0), my_list))
map_final = list(map(lambda x: (x%2==0),my_list))
print(filter_final)
print(map_final)


