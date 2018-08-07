import math

class Circle:
    def __init__(self,han):
        self.han = han
        print("Created!")

    def area(self):
        return self.han * self.han * math.pi

circle = Circle(10)
print (circle.area())
