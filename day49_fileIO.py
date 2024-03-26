#Read file
with open("C:\\Users\\shiva\\PycharmProjects\\GfGpythonLearning\\myfile", 'r') as file:
    mytext = file.read()
    print(mytext)

#Reading by defining the bytes to read from the file
with open("C:\\Users\\shiva\\PycharmProjects\\GfGpythonLearning\\myfile", 'r') as file:
    limittext = file.read(8)
    print(limittext)


#Appendingthe text in the file so we need to open the file in append mode
with open("C:\\Users\\shiva\\PycharmProjects\\GfGpythonLearning\\myfile", 'a') as file:
    file.write("MyLovePuju")


#Creting new file which is not present before so write mode will accomplich the task
# with open("C:\\Users\\shiva\\PycharmProjects\\GfGpythonLearning\\myfile2", 'w') as file:
#     file.write("Puju")
#     file.write("Rai")