
def define_function(j,k):
    sum = j+k
    return sum
addition = define_function(33,52)
print(addition)


def check_even(num):

    if num<=0:
        print("Enter Positive integer Number to check")
    elif num%2==0:
        print(f"{num} is Even Number")

    else:
        print(f"{num} is Odd Number")

check_even(29)


def even_check_list(even_list):
    for numb in even_list:
        if numb%2==0:
            print(f"Number {numb} is Even number in the list")
        else:
            print(f"Number {numb} is Odd number in the list")

list=[13,17,26,39,33]
even_check_list(list)