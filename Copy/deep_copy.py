
'''
A deep copy creates a new compound object before inserting copies of the items found in the original into it in a recursive manner.
It will first construct a new collection object and then recursively populate it with copies of the child objects found in the original.
It means that any changes made to a copy of the object do not reflect in the original object.
'''

import copy

original = [[1, 2, 3], [4, 5, 6]]
deep_copied = copy.deepcopy(original)

# Modifying the copied object
deep_copied[0][0] = 99
print("Deep Copied:", deep_copied)
print(original)


