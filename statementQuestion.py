

st = "Print only words that starts with 's' in this sentence"
print(st.split())
my_st = st.split()

for i in my_st:
    #print(i)
    if i[0] == 's':
        print(i)
    else:
        pass


for i in range(0,11):                      #print even number till 10
    if i%2==0:
        print(i)


divisible_by_3 = [ x for x in range(0,50) if x%3==0 ]    #list comprehension for divisibility by 3 in range of 0 to 50
print(divisible_by_3)

''' Go through the string and if length of word is even print even '''

evn_str = "Here we are trying to keep every word as even but few words are odd Number so lets cater those as well"
print(evn_str.split())
for i in evn_str.split():
    if len(i)%2==0:
        print(f" The length is even: ",i)

    else:
        print(f"The length is odd: ", i)


'''FIZBUZZ Problem for divisible by 3 & 5 in the range of 0 to 100'''

my_list = []
for x in range(0,101):
    if x%3==0 and x%5==0:
        my_list.append("FIZZBUZZ")
    elif x%3==0:
        my_list.append("FIZZ")
    elif x%5==0:
        my_list.append("BUZZ")
    else:
        my_list.append("Neither FIZZ nor BUZZ")

print(my_list)

















