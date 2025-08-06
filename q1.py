names = ['Daksh Sharma','Saurabh Kumar','Aditya Singh','Prajjwal Arya','Prateek asd','Aditya Rana','Harshwardhan Singh','Ayush Raj','Junaid ','Ashok Kumar']

# part a
print("Printing First names => ")
for name in names:
    first_name = name.split(' ')[0]
    print(first_name,end=', ')


# part b
print("\nPrinting Last names => ")
for name in names:
    last_name = name.split(' ')[-1]
    print(last_name,end=', ')


# part c
sliced_names = names[3:6]
print(f"\nSliced Names : {sliced_names}")


# part d
reverse_order = names[::-1]
print(f"Reverse Order: {reverse_order}")



# part e
sliced_reverse = names[8:2:-1]
print(sliced_reverse)

