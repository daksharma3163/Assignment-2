
with open("content.txt", "r+") as file:
    content = file.read()
    print(f"Previous Content of the file:\n{content}")
    file.seek(0)
    file.write("Hi, I am currently pursuing my BTech from Jaypee.")
    file.truncate() 

with open("content.txt", "r") as file:
    updated_content = file.read()
    print(f"\nUpdated Content of the file:\n{updated_content}")
