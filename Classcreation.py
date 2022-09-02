from Class import Developer



def Method1(self):
      print(self.x)

Newclass = type('Newclass',(Developer,),{'x':"madsh",'Method1':Method1})

print(Newclass)
# # print(Newclass().x)
# call= Newclass()

# print(call.x)
# print(call.y)

def echo (Argument):
      print(Argument)

echo(Newclass)
print(hasattr(Newclass,'x'))
print(hasattr(Newclass,'Method1'))
print(Newclass().Method1())