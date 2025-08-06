user_list = input("Enter a list of numbers : ")
numbers = list(map(int, user_list.split()))
print("Printing even numbers from the list: ")
for i in numbers:
    if i % 2 == 0:
        print(i,end=', ')