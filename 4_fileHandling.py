# r is read
# w is write new(!!!)
# a is append !!

fileReadObject = open('./myData','r')
print(fileReadObject.readline(4))
fileReadObject.close()


# create new file and write to it
fileWriteObject = open('./myData_new','w')
fileWriteObject.write("Something\n")
fileWriteObject.close()

# append data to new file
fileAppendObject = open('./myData_new','a')
fileAppendObject.write("Something2\n")

# open first file again (has been closed)
# append content of first file to new file
fileReadObject = open('./myData','r')
for data in fileReadObject:
    fileAppendObject.write(data)
