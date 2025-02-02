
with open('/myfile', 'w') as writer:

    line = ['Shiv', 'completed','50', 'days' , 'of', 'Learning', 'Challenge']
    for x in line:
        writer.write(x+ '\n')
        

    # while True:
    #     line = reader.readline()
    #     if not line:
    #         break
    #     print(line)
    #
