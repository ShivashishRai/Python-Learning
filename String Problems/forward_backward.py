#WAPP to print the input string in forward and backward direction with loop
word = input("Enter the word: ")
counter = 0
print("Word with forward look:")
while counter < len(word):
    print(word[counter],end='')
    counter +=1
print('\n')
print("Word with backward look: ")
counter = -1
while counter >= -len(word):
    print(word[counter],end='')
    counter -=1

print('\n')
#WAP to print in the input string in forward and backward direction using slice and for loop
print("Forward direction word with slice and for loop method")
for x in word[::]:
    print(x,end='')

print('\n')
print("Backward direction word with slice and for loop method")
for x in word[::-1]:
    print(x,end='')