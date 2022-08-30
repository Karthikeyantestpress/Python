class polygon:
    def __init__(self,sides):
        self.sides=sides 
    def Display(self):
        print("You are in polygon")
    def get_perimeter(self):
        perimeter =sum(self.sides)
        return perimeter

