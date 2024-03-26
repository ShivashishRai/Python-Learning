
#Python Program to print Prime Number in a given range.
import math
start_num= int(input(f"Enter the start range to check prime number: "))
end_num = int(input(f"Enter the end range to check prime number: "))
prime_num_list = []                                #Empty list to store all prime number in the range

#to print prime number in the range of start and end number opted by user
print(f"\n The Prime numbers within opted range is:")
for x in range(start_num,end_num+1):                    #Outer loop catering start to end of opted range
    if x>1:
        for i in range(2,int(math.sqrt(x))+1):           #inner loop inorder to identify even/prime number
            if x % i == 0:
                break
        else:
            #print(x, end=" ")                          #to print the numbers on console
            prime_num_list.append(x)                          # Appending prime number in list
    else:                                               #to check wheather start number less than 1
        print("Kindly Enter number greater than !! Try Again")

#print list of prime number
print(prime_num_list)
print(f"Total Primer Number found in the given range is: ",len(prime_num_list))
