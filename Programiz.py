# def Student(Average):
#    print(Average/100)

# def Modfying(func):
#     def Mod(Average,total_sub):
#          Average =Average *total_sub
#          return func(Average)
#     return Mod

# ref =Modfying(Student)
# ref(50,2)
# ref(100,2)


from re import A




def new_Sub(func):
    def Modify(a,b):
        if b>a:
            a,b=b,a
        return func(a,b)
    return Modify
@new_Sub
def Subtraction(a,b):
    Subtract =a-b
    print(Subtract)
    
op =new_Sub(Subtraction)
op(10,20)
    