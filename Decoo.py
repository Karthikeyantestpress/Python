# def Method(Text):
#     return Text+"Success"
    

# Method("We are in Method1")

# Ref =Method
# print(Ref("With reference"))

# S3 = [Ref('List'),2,3,4]
# print(S3)

# S4 = {"We are in method":Ref("HashTable")}
# print(S4)

# def shout(text):
#     print(text)
#     return text.upper()
 
# def whisper(text):
#     print(text)
#     return text.lower()
 
# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print (greeting)
 
# greet(shout)
# greet(whisper)

def create_adder(x):
    def adder(y,z):
        return x+y+z
 
    return adder
 
add_15 = create_adder(15)
 
print(add_15(25,20))
