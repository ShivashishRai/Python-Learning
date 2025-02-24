

def word_freq(word):
    freq_word = {}
    list_word = word.lower().split()

    for x in list_word:
       if x not in freq_word.keys():
           freq_word[x] = 1
       else:
           freq_word[x] += 1

    print(freq_word)


wo_freq = input("Enter the word to count the frequency of words: ")
word_freq(wo_freq)