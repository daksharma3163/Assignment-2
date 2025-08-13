def lensort(lst):
    return sorted(lst,key=len)

def extsort(file_list):
    return sorted(file_list, key=lambda x: x.split('.')[-1] if '.' in x else '')


user_list = input("Enter the string list: ")
user_list = list(map(str,user_list.split()))
print(lensort(user_list))


files = ["report.docx", "data.csv", "image.png", "notes.txt", "archive.zip"]
print(extsort(files))