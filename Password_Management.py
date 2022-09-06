Master_Password = input("Enter your Master password : ")
Flag=  False

def view ():
    with open("Cloud_Password.txt","r") as f:
      print(f.read())

def add():
    Name =input("Account Name :")
    Password=input("Please write a new password :")
    with open("Cloud_Password.txt","a") as f:
        f.write(Name + "!" + Password +"\n")

if Master_Password == "Software_Developer":
   Flag=True
   while(Flag):
      print("Type view to view your password")
      print("Type add to add your password")
      print("Type q to quit from the page ")
      Mode =input("Please type here:   ")

      if Mode =="q":
        print("You have exited the page ")
        break
      if Mode =="view":
        view()
      elif Mode =="add":
        add()
      else:
        print("Invalid option")
else :
   print("Invalid Master_Password : ")
