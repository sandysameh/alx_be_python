class Shape:
    def calculate_area(self):
        print("calculates area of shape")

class Rectange(Shape):
    def calculate_area(self):
        print("calculates are of rectange")


rectange = Rectange().calculate_area()
shape = Shape().calculate_area()
