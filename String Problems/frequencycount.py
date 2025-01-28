

# #WAP to demonstrate each occurrence  of frequency
#
# myword = input("Enter the word to count the frequency of each letter: ")
#
# freq_dict = {}
# for i in myword:
#     if i in freq_dict:
#         freq_dict[i] += 1
#
#     else:
#         freq_dict[i] = 1
#
# print(freq_dict)
#
#
# #WAP demostrate each occurrance of frequency using counter method
#
# # from collections import Counter
# #
# # freq = Counter(myword)
# #
# # print("Word Frequency : \n ", +freq)
#
#
#
# word="Shivashishswatiruchiaditidikshajhupoojagunjanneha"
#
# mygf_word = {}
# for i in word:
#     if i in mygf_word:
#         mygf_word[i] += 1
#
#     else:
#         mygf_word[i] = 1
#
# print(mygf_word)
#
#
# print("********************Another Word Frequency Problem Practise ***********************")
# word = input("Enter the word to count the frequency:").lower()
# fre_word = {}
# for x in word:
#     if x in fre_word:
#         fre_word[x] += 1
#
#     else:
#         fre_word[x] = 1
#
# print("Frequcncy of word is :",fre_word)
#


word_prob = input("Enter the string to count frequency:").lower()

fre_count = {}
total_count = 0

for x in word_prob:
    if x not in fre_count:
        fre_count[x] = 1
        total_count +=1
    else:
        fre_count[x] += 1
        total_count += 1

print(fre_count)
print(total_count)

