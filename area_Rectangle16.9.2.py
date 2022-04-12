class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

area_Rectangle = Rectangle(25, 40)
print('Площадь прямоугольника', area_Rectangle.get_area(), 'ед')
