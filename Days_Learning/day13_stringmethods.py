
#Strings are immutable
name = "Shivashish"
upper_name = name.upper()   #converting to uppercase
lower_name = name.lower()
print(upper_name)        #name in upper case
print(lower_name)

#strip method remove the matching char
stripname = " Shivas!!!!!"
print(stripname.strip('!'))
print(stripname.rstrip('!'))
print(stripname.lstrip(' '))

#splits the char into a list on the basis of first match char defined
sep = stripname.split('a')
print(sep)

#repalce method replaces all occrances of the provided matching variable
print(name.replace('a','A'))

#Title : convert each word first letter to upper case
tit = "shivash is Trying hard To Code in PYTHON"
print(tit.title())

#count the each occurance of the letter
print(tit.count('a'))

print(tit.capitalize())
print(tit.endswith('PYTHON'))
print(tit.isprintable())
print(tit.swapcase())


