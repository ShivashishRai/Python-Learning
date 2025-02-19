
#WAP to reverse list

my_list = [31,22,17,33,19,23,18]

#reverse built in method
# my_list.reverse()
# print(my_list)

#Slice operator
slice_list = my_list[::-1]
print(slice_list)

#reversed built in method
reversed_list = list(reversed(my_list))
print(reversed_list)

#reverse through loop
for_rev_list = []
for x in range(len(my_list)-1,-1,-1):
    for_rev_list.append(my_list[x])

print(for_rev_list)
