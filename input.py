Name  = input("Enter your Nmae : ")
Age = int (input("Enter your age :"))
print("Welcome to Testpress " + Name )
if (Age>18) and (Age<100):
  print("You are eligible to vote")
elif(Age<18)and (Age> 0):
  print("You are not eligible to vote")  
else:
  print("Invalid number")