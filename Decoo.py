def Method(Text):
    return Text+"Success"
    

Method("We are in Method1")

Ref =Method
print(Ref("With reference"))

S3 = [Ref('List'),2,3,4]
print(S3)

S4 = {"We are in method":Ref("HashTable")}
print(S4)