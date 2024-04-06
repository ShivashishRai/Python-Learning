

rev_string = input("Enter string : ")

rev = list(reversed(rev_string))
print(''.join(rev))


# ******************************************************** #

string = "My Learning Journey is Something i am loving it"

s = string.split()[::-1]
l=[]
print(s)
for x in s:
    l.append(x)

print(' '.join(l))
