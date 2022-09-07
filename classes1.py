class One:
    x=100
    y=200

print("Before Main")

if __name__ =="__main__":
    Reference =One()
    print(Reference.x)
    print(Reference.y)
else :
    print ("else part")
