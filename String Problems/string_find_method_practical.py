
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


print("****************************************************************")
while True:
    first_count = word.find(sub_word,start_pos,word_len)
    if first_count == -1:
        exit()

    else:
        print(f"Found the sub string {sub_word} at position:", first_count)
        start_pos = first_count + len_sub_word
        count += 1








