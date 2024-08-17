
#WAP to remove space from the string and count the number of spaces in the string
originar_string = input("Eneter the long string :")
remove_spaces = originar_string.replace(' ','')
print("The sapces are removed from string:", remove_spaces)

spaces_removed = len(originar_string)-len(remove_spaces)
print("The count of spaces removed from original string is :", spaces_removed)