

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
