from math import pi


class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def get_area(self):
        return round(pi * (self.radius **2))

    def get_perimeter(self):
        return round(pi * 2 * (self.radius **2))


circy = Circle(11)
print(circy.get_area())