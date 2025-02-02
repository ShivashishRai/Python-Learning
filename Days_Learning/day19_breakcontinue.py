
for x in range(11):
    if x == 7:
        #break        #it will skip the loop iteration/exit loop
        continue      #it will skip the curent iteration
    print("5 x" ,x,"=" , (5*x))

#same problem with the help of while loop
i=1
while i in range(11):
    if i ==7:
        break    #break the iteration
    print(5*i)
    i += 1