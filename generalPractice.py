from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()

def main():
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    print(Fruit.APPLE.name, Fruit.APPLE.value)

    print(Fruit.PEAR.value)

    myfruits = {}
    myfruits[Fruit.BANANA] = "I am waiting for you to turn yellow."
    print(myfruits)


if __name__ == "__main__":
    main()