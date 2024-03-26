

def reverse_words(string):

    rev_word = ''
    word = string.split()
    for i in word:
        rev_word = i[::-1]
        print(rev_word, end= " ")

#if __name__ == '__main__':
user_word = input("Enter the sentece to be reverse: ")
reverse_words(user_word)