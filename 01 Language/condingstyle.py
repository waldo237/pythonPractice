import sys
import os

class MyClass():
    def __init__(self):
        self.prop1 = "my class"

    def method1(self, arg1):
        pass
def main():
    cls1 = MyClass()
    cls1.prop1 = "Hello world"

if __name__ == "__main__":
    main()