user_list = input("Enter a list of numbers : ")
numbers = list(map(int, user_list.split()))


duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print(duplicates)