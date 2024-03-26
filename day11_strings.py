
name = input("Enter word to check palindrome: ")
#print(name)

#reverse of the strint
s = name[::-1]
#jumping 2 char of the string
t = name[::2]

print(t)
# for x in s:
#     print(x)

if name == s:
    print("Palindrome")

else:
    print("No Palindrome")

#Multiline string '''enclosing statment ''' in """enclosing statement """"
# mult_line = '''My name is Shivashish
#  I have been workding not hard enough
#  for my golas'''
# print(mult_line)

print(name[3])
print(len(name))
print(name[len(name)-4])
