
#List Comprehension : way of creating list object from any iterable objects (list, tuple, set,dict, range etc) based on some specific conditions

l = [x for x in range(10)]
print(l)

odd_list = [x for x in range(60) if x%2 !=0]
print("Odd Numbers till 60 are as follows: ",odd_list)

square = [x**2 for x in range(20) if (x**2)%2==0]
print("The Number with even number as square till 20 are as follows: ",square)


list1 = [11,13,17,19,18]
list2 = [13,23,18,24]

unq_list = [x for x in list1 if x not in list2]
print(unq_list)

comm_list = [x for x in list1 if x in list2]
print(comm_list)


#WAP to get the list with word and word len into a nested list concept
statm = "The Quick Brown Fox Jump Over the Lazy Dog"
statms = statm.split()
word_len = [[word,len(word)] for word in statms ]
print(word_len)