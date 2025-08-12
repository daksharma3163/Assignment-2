def group(lst, size):
    result = []
    for i in range(0, len(lst),size):
        part = lst[i:i+size]
        result.append(part)
    return result

user_list = input("Enter the list: ")
user_list = list(map(int, user_list.split()))
print(group(user_list,4))
