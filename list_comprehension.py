
#Print even number from user provided list through list comprehension
num = [1,31,22,34,56,67,22,34,56,83,26,39,42]
even_num = [x for x in num if x%2==0]
print(even_num)


''' WAP to print sqare of number through list comprehension '''
square = [x**3 for x in range(20) if x>12]
print(square)

'''WAP to create Matrix of 3*4 through list comprehension '''

matrix = [[j for j in range(4)] for i in range(4)]
print(matrix)

''' Reverse each word with list comprehension and lambda function '''
string = input("Enter the sentence to be reverse: ")
list_strint = string.split()
my_word = [string[::-1] for string in (list_strint)]
print(' '.join(my_word))


''' Creating List of tuple from two seprate lists '''

first_name = ['Shiva', 'Puju']
last_name = ['Rai','Kumari']

dict = [zip(first_name,last_name)]
print(dict)
# first_last = [(first,last) for first ,last  in zip(first_name,last_name)]
# print(first_last)
# #
# first_last_dict = [{first:last} for first,last in zip(first_name,last_name)]
# print(first_last_dict)