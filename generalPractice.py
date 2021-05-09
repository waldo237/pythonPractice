class Color():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return f"rgb({self.red},{ self.green}, {self.blue})"
        elif attr == "hexcolor":
            return f"#{self.red:02x}{self.green:02x}{self.blue:02x}"
        else:
            raise AttributeError

    def __setattr__(self, attr, value):
        if attr == "rgbcolor":
            self.red = value[0]
            self.green = value[1]
            self.blue = value[2]
        else:
            super().__setattr__(attr, value)

    def __dir__(self):
        return ("rgbcolor", "hexcolor")

def main ():
    cls1 = Color()
    print(cls1.rgbcolor)
    print(cls1.hexcolor)
    cls1.rgbcolor = (125, 200, 86)
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # access a regular attribute
    print(cls1.red)
if __name__ == "__main__":
    main()