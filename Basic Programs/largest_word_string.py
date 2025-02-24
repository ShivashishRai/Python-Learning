
#WAP to find the longest word in a sentence

org_sents = input("Enter the Sentence: ").lower().split()
lar_word_org_sents = " "

for word in org_sents:
    if len(word) > len(lar_word_org_sents):
        lar_word_org_sents = word

print(len(lar_word_org_sents))
print(lar_word_org_sents)