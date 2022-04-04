# read sample.txt and print the number of lines

file = open("sample.txt", 'r')
data = file.readlines()
file.close()
print(len(data))
