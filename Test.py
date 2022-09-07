def Hello(Arg):
  def Againhello():
     print("We are in 1")
     Arg()#def NewHello():
             # print("We are in 1.5")
     print("We are in 2")
     Arg()
  return Againhello

def NewHello():
    x=100
    print("We are in 1.5",x)
    
Ref =Hello(NewHello)
Ref()
  
