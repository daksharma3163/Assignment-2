with open("content.txt",'r') as file:
    content = file.read()
    char_count = {}
    for char in content:
        char_count[char] = char_count.get(char, 0) + 1

    print(f"Total characters: {len(content)}")
    print("Character occurrences:")
    for char, count in char_count.items():
        print(f"'{char}': {count}",end=' ')
