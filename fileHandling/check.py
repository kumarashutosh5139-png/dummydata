import os 

os.remove("note.txt")

if os.path.exists("note .txt"):
   print("file exits")

else:
    print("not found")