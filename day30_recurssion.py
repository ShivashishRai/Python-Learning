

def facto(num):
    if num ==1 or num == 0:
        return 1

    elif int(num)>1:
        return num * facto(num-1)

num=int(input("Enter the number to calculate factorial: "))
fact = facto(num)
print(fact)
