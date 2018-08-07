class Triangle:
    def __init__(self,tei,height):
        self.tei = tei
        self.height = height
        print("Created!")

    def culcurate_area(self):
        return self.tei * self.height / 2

t = Triangle(10,20)
print (t.culcurate_area())
