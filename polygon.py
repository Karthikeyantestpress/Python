class polygon:
    def __init__(self,sides):
        self.sides=sides 
    def Display(self):
        print("You are in polygon")
    def get_perimeter(self):
        perimeter =sum(self.sides)
        return perimeter

class Triangle(polygon):

    def Display(self):
        print("A Triangle is a polygon with edges"
        )

class Quadrilateral(polygon):

   def Display(self):
        print("We are in Quadrilateral")

t1=Triangle([5,6,7])
perimeter=t1.get_perimeter()
print(perimeter)