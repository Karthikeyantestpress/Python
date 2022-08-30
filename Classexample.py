class Triangles:

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def Triangle(self):
      Result= self.a+self.b+self.c
      return Result 
T1= Triangles(3,4,5)
print(T1.Triangle())
      