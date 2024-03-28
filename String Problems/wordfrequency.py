

#WAP to count each word frequency from user input sentence


def freq(sent):

    sents = sent.split()
    print(sents)
    sents2 = []
    for i in sents:
        if i not in sents2:
            sents.append(i)

    for i in range(0, len(sents2)):
        print("Count of", sents2[i],"in the sentence is", sents.count(sents2[i]))

def main():

    sent = input("Enter the sentence to get the frequency of each word: ")
    freq(sent)

if __name__ == "__main__":
    main()