
# #File Handling :
#
# #Type of Files
#     #1. text files:
#     #2. Binary Files:
#
# #Text Files
#     # Allowed mode : r- read ,w-write ,a-append ,r+ - to read and write and won't overwrite existing data ,
#     # w+ - write and read also it will overwrite existing data ,a+ - append and write also it won't overwrite existing data ,x - exclusive creation mode (only used when file is not existing already)
#
#
#     #Opening of a file is first step
# file_read = open('myfirst_file','r')       # read the text from existing file
# #print(file_read.readlines())
# print(file_read.read())           #to read the conent of the file
# print(type(file_read))
# #file_read.close()                 #to close the already open file
#     #it's mandatory or best practice to close the file once you're done else file will be corrupted
# #print(file_read.read())
#
#
# #Properties of File Object
# print(file_read.name)          # to get the name of opened file
# print(file_read.closed)        # to get whearther the file is closed or not (True/False)  uncomment  line 18 to get 'False'
# print(file_read.mode)          # to get mode in which file is opened
# print(file_read.readable())    # Returns True if file is readable
# print(file_read.writable())    # Returns True if file is writeable

# #Operations on File
# file_read = open('myfirst_file','a+')
# file_read.write("\t ")
# file_read.write("New Line is going to be added : \t")  #to write single line in file "\t " will add new line
# file_read.write("More Lines are added")
#
# print(file_read.read())
# file_read.close()
#
# file_read = open('myfirst_file','w')
# student_name = ('Aman \n','Priya \n','Riya \n','Sikha \n','Jyoti \n','Shruti')
# file_read.writelines(student_name)
# file_read.close()
#
# #print(file_read.read())
#
# #Reading data from file
#
# #read() -  to read complete file
# #read(n) - to read n char from file
# #readline() - read only one line
# #readlines() - to read all lines into a list
# file_read = open('myfirst_file','r')
# print(file_read.read(10))
# #print(file_read.readline())
# print(file_read.readlines())
#
#
# #seek() - to reset the file pointer to given position
# print(file_read.read())
# file_read.seek(10)       #this will point the pointer to 10th position again
# print(file_read.read(11))


# #WAP to read file content till last line is reached
# file_read = open('myfirst_file','r')
# line = file_read.readline()
# while line != '':
#     print(line, end='')
#     line = file_read.readline()
# file_read.close()


#with : inorder to open and close the file we can utilise with which automatically closes the file once program is done successfully, this will enhance the performance

with open('myfirst_file','w') as write_file:
    write_file.write('Shikha\nBittu\nTuk-Tuk')
    print(write_file.closed)         #file is opened as this is within with block

print(write_file.closed)             #file is closed automatically as stateemnt is written outside with block