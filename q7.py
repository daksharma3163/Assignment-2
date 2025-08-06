a,b = 0,1
print("Fibonacci till 5th term: ")
for i in range(500):
    print(a,end=', ')
    a,b = b, a + b

