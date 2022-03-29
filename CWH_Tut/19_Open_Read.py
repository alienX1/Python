f = open("20_file.txt","rt")

# print(f.readlines())  # Returns a list object
# print(f.readline())  # This will return the string

# content = f.read()

# for line in f:
#     print(line, end="")
# print(content)

content = f.read(666)
# print("2", content)

f.close()

print(content)

