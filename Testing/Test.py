import re 
'''We can Test a code before implementing it into our 
original project and check for all bugs and recode if 
anyand can add finally once it is  free of buy this 
process is Test Driven Developement '''

'''Code to vaidate the studednts name only if it contains numbers and letters'''

Student_Name=input("Please Enter your Name : ")

pattern = re.compile(r'^[a-zA-Z]+$')
matches =pattern.search(Student_Name)

if matches :
    print ("Your Name is stored successfully as : "+Student_Name)
else :
    print ("Invalid enter kindly only use words without number or special character")
