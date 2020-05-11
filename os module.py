import os,sys
fname=input("Enter file name")
if os.path.isfile(fname):
    print("file is exist")
else:
    print("file is not exist")
    sys.exit(0)
    
