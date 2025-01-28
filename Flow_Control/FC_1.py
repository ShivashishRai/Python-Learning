
#Order in which PVM is going to execute the Code

'''
Conditional
Iterative
Transfer
'''

#Conditional

#Iterative Statement
'''
for x in expression:
    body

while():
    body

'''
#Nested Loop
# for i in range(4):
#     for j in range(4):
#         print(i,j)
#
# #Patterns Programming Concept
#
# #Print * as per user input in same line
# for x in range(5):
#     for j in range(5):
#         print("*",end=" ")


# #Square Pattern
# i=int(input("Enter no of rows"))
# for x in range(i):
#     for j in range(i):
#         print("*",end=' ')
#     print()

# #WAP to print sequential progress in row and column eg below
# '''
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# '''
# i = int(input("Enter no of rows"))
# for x in range(1,i+1):
#     for j in range(i):
#         print(x, end=' ')
#     print()


#WAP to print sequential progress in row and column eg below
'''
A A A A
B B B B 
C C C C
'''
i = int(input("Enter no of rows"))
for x in range(0,i+1):
    for j in range(i):
        print(chr(65+x), end=' ')
    print()