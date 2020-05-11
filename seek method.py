data="How are u? Hello Venky Naidu .... How are u murali kshdjhkhdka"
f=open("madhavi.txt","w")
f.write(data)
with open("madhavi.txt","r+") as f:
    text=f.read()
    print(text)
    print("Present position of the pointer:",f.tell())
    f.seek(10)
    print("Now the cursor moved to:",f.tell())
    text2=f.read(5)
    print(text2)
    
