with open('content.txt','r') as file:
    content = file.readlines()
    print(f"Previous Content\n{content}")
    
    for line in reversed(content):
        print(line.rstrip())


