from math import pi
class Shape:
    def __init__(self) -> None:
        pass
    def area(self):
        raise NotImplementedError(f"derived classes need to override this method")
    
class Rectangle(Shape):
    def __init__(self, length, width):
             super().__init__()
             self.length = length
             self.width = width
    def area(self):
         area = self.length * self.width
         return f"The area of the Rectangle is: {area}"
             

class Circle(Shape):
     def __init__(self, radius):
          #super().__init__()
          self.radius = radius

     def area(self):
          area = pi * self.radius ** 2 
          return f"The area of the Circle is: {area}"