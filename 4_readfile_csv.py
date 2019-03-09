import csv

# open file and write content to console
print("-----------------------------------")
with open('E:/Dev/python/default/fakeFile.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

    print(csv_reader) # prints objects memore space

# prints:
# ['jane', ' doe', ' janedoe@web.de']
# ['john', ' mayer', 'john@web.de']
# ['sepp', 'sepp', ' sepp@sepp.de']

print("-----------------------------------")
with open('E:/Dev/python/default/fakeFile.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader) # skips one/first line

    for line in csv_reader:
        print(line)

# prints:
# ['john', ' mayer', 'john@web.de']
# ['sepp', 'sepp', ' sepp@sepp.de']

# read old file and save to new file with different delimiter
print("-----------------------------------")
with open('E:/Dev/python/default/fakeFile.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('E:/Dev/python/default/fakeFile_new.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t') # tab als delimiter

        for line in csv_reader:
            csv_writer.writerow(line)

# read new file
with open('E:/Dev/python/default/fakeFile_new.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)


# read via dictreader
print("-----------------------------------")
with open('E:/Dev/python/default/fakeFile.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)
        print(line['email'])




# read old file and save to new file with different delimiter
# now with DictReader
print("-----------------------------------")
with open('E:/Dev/python/default/fakeFile.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    with open('E:/Dev/python/default/fakeFile_newDict.csv', 'w') as new_file:
        fieldNames = ['first-name', 'last-name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldNames, delimiter='\t') # tab als delimiter

        csv_writer.writeheader()
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)

with open('E:/Dev/python/default/fakeFile_newDict.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)
