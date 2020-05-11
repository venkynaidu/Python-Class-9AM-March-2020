#program to open file and write some text with the help of with statement

with open("madhavi.txt","w") as f:
    f.write("Hello\n")
    f.write("Good Morning")
    print("is file close",f.closed)
print("is file closed after operation:",f.closed)
    
