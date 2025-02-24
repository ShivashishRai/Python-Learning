'''
A shallow copy creates a new object but retains references to the objects contained within the original.
It only copies the top-level structure without duplicating nested elements.
Changes made to a copy of an object do reflect in the original object.
In python, this is implemented using the “copy.copy()” function.
'''

import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)

# Modifying the copied object
shallow_copied[0][0] = 99
print("Shallow Copied:", shallow_copied)  # Output: Shallow Copied: [[99, 2, 3], [4, 5, 6]]

print(original)