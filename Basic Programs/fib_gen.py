
#WAP to print the febonacci series using generator

def fib_gen():

    first = 0
    second = 1

    while True:
        temp = first
        first = second
        second = temp + first

        yield temp

fibonnaci_series = fib_gen()
for x in range(10):
    print(next(fibonnaci_series) , end= " ")

# WAP to print fibonacci series without using gen function
#
# def fib_num(num):
#     firs_t = 0
#     secon_d = 1
#     for x in range(num):
#         tem_p = firs_t
#         firs_t = secon_d
#         secon_d = tem_p + firs_t
#
#     return secon_d
# fib = []
# fib = fib.append(fib_num(7))
# print(fib)
