with open('example.txt', 'w') as file:
    file.write("This is the first line.\n")
    file.writelines(["This is the second line.\n", "This is the third line.\n"])

with open('example.txt', 'r') as file:
    content = file.read()
    print("Content using read():")
    print(content)


with open('example.txt', 'r') as file:
    print("Content using readline():")
    line = file.readline()
    while line:
        print(line, end='') 
        line = file.readline()

