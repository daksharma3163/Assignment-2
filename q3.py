students = {
    "Alice": 19,
    "Bob": 22,
    "Charlie": 21,
    "David": 18
}

# part a
print("Students older than 20:")
for name, age in students.items():
    if age > 20:
        print(f"{name}: {age}")


# part b
students["Eve"] = 30
print("\nAdded Eve with age 30.")

# part c
print("\nAll students:")
for name, age in students.items():
    print(f"{name}: {age}")

# part d
del students["Charlie"]
print("\nDeleted Charlie.")

# part e
average_age = sum(students.values()) / len(students)
print(f"\nAverage age of students: {average_age:.2f}")