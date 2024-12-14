import os 

file = open("myData.txt", "w")
file.write("Hello World")
file.close()

# reading a file

file = open("myData.txt", "r")
data = file.read()
print(data)
file.close()

# combination of reading and writing in a file

file = open("myData.txt", "r+")
data = file.read()
print(data)
file.write("\nThis is a new line")
file.close()