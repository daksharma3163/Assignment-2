names = ('Daksh Sharma','Saurabh Kumar','Aditya Singh','Prajjwal Arya','Prateek')

# part a
for name in names:
    print(name,end = ', ')

# part b
name = input("\nEnter a new name : ")
names = names + (name, )
print(names)

# part c
name_list = list(names)
name_list.remove('Prateek')
names = tuple(name_list)
print(names)

# part d
print(names[1:4])

# part e
new_list = list(names)
name = input("Enter a name : ")
print("After modifying second index =>")
new_list[2] = name
names = tuple(new_list)
print(names)