from triangle import Triangle
from polygon import polygon


class Quadrilateral(polygon):

   def Display(self):
        print("We are in Quadrilateral")

t1=Triangle([5,6,7])
perimeter=t1.get_perimeter()
print(perimeter)