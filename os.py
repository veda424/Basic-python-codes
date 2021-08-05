import os

def finding(filename , find):
    with open(filename , "r") as f:
        filecontent = f.read()
        
        if find in filecontent:
            print(f"{find} is present in {filename} file: ")
        if find not in filecontent:
            print(f"{find} is not present in {filename} file")



files = os.listdir()
find = input("enter string to find : ")
for sfile in files:
    if sfile.endswith(".txt"):
        finding(sfile , find )

   