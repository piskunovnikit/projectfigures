class Rectangle:
    def __init__(self, x, y, width, heigh):
        self.x = x
        self.y = y
        self.width = width
        self.heigh = heigh
    def get_area(self):
        return f'( x = {self.x},  y = {self.y}, Ширина  = {self.width}, Высота  = {self.heigh})'
randomrectangle = Rectangle (3, 2, 30, 90)
print(randomrectangle.get_area())