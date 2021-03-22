import sys

class Square:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    def area(self):
        return self.width * self.length
    
r = Square(43, 54)
print("square area: %dft" %(r.area()))

print(sys)