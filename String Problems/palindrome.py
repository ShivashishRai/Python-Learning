
#WAP to Wo
mystring='Delhi'
new_mystring = mystring[::-1]
print(new_mystring)

if mystring == new_mystring:
    print("Palindrome")

else:
    print("Not Palindrome")


#inbuild function to check the palindrome

def ispalindrome(s):

    sr =''.join(reversed(s))
    if s == sr:
        return True
    else:
        return False

str="malayalam"
boo = ispalindrome(str)
if (boo):
    print("Palindrome")
else:
    print("Not palindrome")
