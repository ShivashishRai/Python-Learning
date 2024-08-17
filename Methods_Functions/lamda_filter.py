

#WAP to  filter the sequence of list

def my_even_num(num):
    if num%2==0:
        return True
    else:
        return False

li_num = [2,5,7,8,11,13,14]
my_filter_obj = list(filter(my_even_num,li_num))
print(my_filter_obj)



#WAP to convert above program into lamda function
lamda_even_num = list(filter(lambda n:n%2==0,li_num))
print(lamda_even_num)

#WAP to return app items with length of 3 or more than 3 using lamda function

word_len = ('A','AB','ABC','ABCD','ABCDE','ABCDEF','ABCDEFG','ABCDEFGH')

word_with_len_4 = list(filter(lambda x:len(x)%4==0,word_len))
print(word_with_len_4)





