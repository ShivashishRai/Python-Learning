
'''Function to get the prime number in user defined range of number'''

def prime(x,y):
    prime_no = []
    #iterrating over the range defined by user
    for i in range(x,y):
        #checking wheather the number is 0 or 1
        if i ==0 or i ==1:
            continue
        else:
            for j in range(2, int(i//2)+1):                    # getting the half of the number
                if i % j == 0:
                    break
            else:
                prime_no.append(i)                              # appending the prime number to an empty list defined at start of program
    return prime_no

#asking user to enter start and end range
start_range = int(input("Enter the starting range to check prime number: "))
end_range = int(input("Enter the ending range to check the prime number :"))

#calling prime number function
prime_list=prime(start_range,end_range)
print(prime_list)
#getting the count of prime number list found ini the range
count_of_prime = len(prime_list)

if count_of_prime <=0:
    print("No prime number is found in the given range")

else:
    print(f"List of Prime no. {prime_list}")
