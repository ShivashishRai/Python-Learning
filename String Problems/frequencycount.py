

#WAP to demonstrate each occurrence  of frequency

myword = input("Enter the word to count the frequency of each letter: ")

freq_dict = {}
for i in myword:
    if i in freq_dict:
        freq_dict[i] += 1

    else:
        freq_dict[i] = 1

print(freq_dict)


#WAP demostrate each occurrance of frequency using counter method

# from collections import Counter
#
# freq = Counter(myword)
#
# print("Word Frequency : \n ", +freq)



word="Shivashishswatiruchiaditidikshajhupoojagunjanneha"

mygf_word = {}
for i in word:
    if i in mygf_word:
        mygf_word[i] += 1

    else:
        mygf_word[i] = 1

print(mygf_word)