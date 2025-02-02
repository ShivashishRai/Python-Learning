

import os

#to check LearnTime directory already existing or not
# if (not os.path.exists("LearnTime")):
#     os.mkdir("LearnTime")
#
# #to create folder insided the LearnTime folder above created
# for i in range(2,5):
#     os.mkdir(f"LearnTime/Day {i+1} ")

folders = os.listdir("LearnTime")
print(folders)
os.remove('LearnTime/Day 2')


# print(os.getcwd())
# folders = os.listdir("Number Problem")
# print(folders)

# #os.chdir("/LearnTime")
# print(os.getcwd())
#
# file = 'LearnTime/'
# myfile = 'Day 2'
# path = os.path.join(file,myfile)
# os.remove(path)