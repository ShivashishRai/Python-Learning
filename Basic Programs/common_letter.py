
#WAP to find common letters b/w two string

def common_letter():
    str1 = input("Enter First string: ").lower().split()
    str2 = input("Enter Second String: ").lower().split()

    s1 = set(str1)
    s2 = set(str2)

    common = s1 & s2
    print("Common letters b/w two words are :",common)

common_letter()