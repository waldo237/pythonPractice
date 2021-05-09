import sys
import os

class ClassP:
    def __init__(self):
        self.prop =  "a new thing."
    
    def method1(self, arg):
        pass


def main():
    cls = ClassP()
    cls.prop = 'not really'
    b = bytes([0x32,0x49, 0x43, 0x21])
    print(b)

    s = "my first string"
    print(s)

    s2 = b.decode('utf-8')
    print(s+s2)

    b2 = s.encode('utf-8')
    print(b2)


if __name__ == "__main__":
    main()