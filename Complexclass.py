class complex:
     def __init__(self,real,image):
          self.real=real
          self.image=image

     def add(self,number):
          real=self.real+number.real
          image=self.image+number.image
          result=complex(real,image)
          return result 

     def __str__(self):
          return "The real part {} and imaginary part {}".format(self.real,self.image)

n1 = complex(1,3)
n2 = complex(-4,3)
result = n1.add(n2)
print(result)
