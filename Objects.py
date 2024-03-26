

print("The Value of {d} {c} {r}".format(r="ruppe", c="china dollar" , d = "Us dollar"))

list1 = ["One", 2 , 2.9]
list2 = ["two", "four", "##&!#"]

new_list = list1+list2
print(new_list)
print(list1[2])

print(list1[1:])

new_list[3] = 4.88
print(new_list[3:])

list3 = [32,11,16,1,37,4]
list3.sort(reverse=True)
print(list3)




d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2][0])