
def prime(x,y):
    prime_no = []

    for i in range(x,y):

        if i ==0 or i ==1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                    prime_no.append(i)
    return prime_no

start_range = int(input("Enter the starting range to check prime number: "))
end_range = int(input("Enter the ending range to check the prime number :"))

prime_list=prime(start_range,end_range)
count_of_prime = len(prime_list)

if count_of_prime <=0:
    print("No prime number is found in the given range")

else:
    print(f"List of Prime no. {prime_list}")
