


check_num = int(input("Enter the number you want to check prime :"))
if check_num == 0 or check_num ==1:
    print(f"{check_num} is prime")

else:
    for i in range(2,int(check_num//2)+1):
        if check_num %i !=0:
            print(f"{check_num} No is a Prime number")
            break

    else:
        print(f"{check_num} is not Prime Number")


