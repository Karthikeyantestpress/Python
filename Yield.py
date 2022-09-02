My_List=[1,3,4,5,6,7,7,8,8,9,"bala",10.5]

print("Normally printing a list :",My_List)

for iteration in My_List:
    print("Iterating with for loop: ",iteration) 

mylist = [x*x for x in range(3)]
for i in mylist:
    print(i)

def Generator():
    My_List =range(3)
    for i in My_List:
        yield  i*i

New_Generator =Generator()
print(New_Generator)
for i in New_Generator:
    print(i)
