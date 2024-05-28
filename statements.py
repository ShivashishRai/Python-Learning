
x = 0
while x<6:
    print(f"The value of ",x)

    x = x+1

y = 1
while y < 11:
    product = int(13* y)
    print(f"The Product of 13*{y} = ", product)
    y+=1


def product(x):
    z = 1
    while z < 11:
        multiply = x * z
        print(f"The product of {x} * {z} = ", multiply)
        z+=1

product(19)


g = 10
while g>=0:
    for i in g:
        print("x")

    g-=1

