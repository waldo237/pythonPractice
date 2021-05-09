class Person():
    def __init__(self):
        self.fname = "Carlos"
        self.lname = "Martinez"
        self.age = 25

    def __repr__(self):
        return f"<Person Class -fname:{self.fname}, lname:{self.lname}, age:{self.age}>"

    def __str__(self):
        return f"Person ({self.fname}, {self.lname} is {self.age})"
    def __bytes__(self):
        val =  f"Person:{self.fname}:{self.lname}:{self.age}"
        return bytes(val.encode('utf-8'))

def main():
    cls1 = Person()

    print(repr(cls1))
    print(str(cls1))
    print(f"Formatted: {cls1}")
    print(bytes(cls1)) 

if __name__ == "__main__":
    main()