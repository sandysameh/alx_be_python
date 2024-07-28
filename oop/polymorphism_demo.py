import math

class Shape:
    def area():
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self,length,width) :
        self.length= length
        self.width = width 
    def area(self):
        return self.width * self.length

class Circle(Shape):
    def __init__(self,radius) :
        self.radius= radius
    def area(self):
        return self.radius * self.radius * math.pi
