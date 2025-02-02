
# name = input("Enter the name of the user to find list of vowels :")
# for x in name:
#     if x in "aeiou":
#         print(x,"is vowel")
#     else:
#         print(x)

fav_color = ['Red', 'Orange', 'Yellow', 'Blue', 'Purple']
for color in fav_color:
    #print(color)
    #print(color[0:len(color)-2])
    for i in color:
        print(i)

    print('\n')


for i in range(0,100,4):
    if i == 0:
        print("Number is 0")
    elif i % 7 ==0:
        print("Number",i,"is divisible by 7 ")
    else:
        print(i)