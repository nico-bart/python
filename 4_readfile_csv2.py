import csv

# open file and write content to console
print("-----------------------------------")
with open('E:/Dev/python/default/fakeFile_new.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
