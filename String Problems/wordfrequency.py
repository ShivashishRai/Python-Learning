

#WAP to count each word frequency from user input sentence
def freq(sent):
    sents = sent.split()
    print(sents)
    sents2 = []
    for i in sents:
        if i not in sents2:
            sents2.append(i)

    for i in range(0, len(sents2)):
        print("Count of", sents2[i],"in the sentence is: ", sents.count(sents2[i]))

def main():

    sent = input("Enter the sentence to get the frequency of each word: ")
    #India is densely populated country population being lot of problem to India to overcome problem India need to address lot pf problem to cater its population

    freq(sent)

if __name__ == "__main__":
    main()


print("*******************************************************")
my_list=input("Enter the string to count freq of words:").split()
freq = {}
for item in my_list:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)
# for key, value in freq.items():
#     print("%s : %s" %(key, value))
#     print(freq)