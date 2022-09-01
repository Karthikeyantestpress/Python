import os

current_dir =os.getcwd()

print(current_dir)

os.chdir("/home/karthik/Program2.md")

current2_dir =os.getcwd()

print(current2_dir)

with open ("Directorycheck.py","a") as f:

    f.write("#This file has been moved to Prorgram2 directory")
