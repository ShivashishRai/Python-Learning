

# Reverse each string in tuple

List = [string[::-1] for string in ('Geeks', 'Shiv','for', 'Geeks')]

# Display list
print(List)


#new approach

word = input("Enter the word to reverse")
list_word = word.split()
rev_List = [list_word[::-1] for string in range(len(list_word))]
#Output: 'skeeG', 'vihS', 'rof', 'skeeG'

print(rev_List)
