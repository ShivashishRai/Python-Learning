

def reverse_words(string):

    rev_word = ''
    word = string.split()
    print(word)

    #iterating over the list and reversing each word.
    for i in word:
        rev_word = i[::-1]
        print(rev_word, end= " ")

#if __name__ == '__main__':
user_word = input("Enter the sentece to be reverse: ")
reverse_words(user_word)



# def rev_word(word):
#     final_rev_word = ''
#
#     word_list = word.split()
#     for x in word_list:
#         final_rev_word = x[::-1]
#         print(final_rev_word,end=' ')
#
#
#
# my_word = input("Enter the word to be Reverse: ")
# rev_word(my_word)