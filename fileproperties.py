#program to check the properties of opened file
f=open("venky.txt","r")
print("File name:",f.name)
print("File mode:",f.mode)
print("Is file Readable:",f.readable())
print("Is writable:",f.writable())
print("Is file is closed:",f.closed)

