

with open('C:\\Users\\shiva\\PycharmProjects\\GfGpythonLearning\\myfile','r') as reader:
    #print(reader.read())

    #seek function it helps you to move the current position whitin a file to a specific point.
    # reader.seek(10)
    # print(reader.read())

    #tell function returns the current position within the file in bytes.

    reader.seek(10)
    mycurrentposition = reader.tell()
    print(reader.read(mycurrentposition))