class Circle:
    def __init__(self, radius):
        self.radius = radius
     
    def Area(self):
        return (22/7) * self.radius ** 2
        

    def Perimeter(self):
       return 2 * (22/7) * self.radius
        


cls = Circle(50)
print(cls.Area())
print(cls.Perimeter())