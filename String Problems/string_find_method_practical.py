
#WAP to find all occurrances of sub string into user given string and position also in the string
#Print the occurances of the sub string in the main string

word = input("Enter the string :")
sub_word = input("Enter the sub string to be searched: ")
word_len = len(word)
len_sub_word = len(sub_word)
count = 0
start_pos = 0

while True:
    first_index = word.find(sub_word,start_pos,word_len)
    if first_index ==-1:
        exit()
    else:
        print("Found the sub string at index : ",first_index)
        start_pos = first_index + len_sub_word
        count += 1










