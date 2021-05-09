

def filterFunc(x):
    if x % 2 == 0:
        return False
    return True


def filter2(x):
    if x.isupper():
        return False
    return True


def sqFunc(x):
    return x**2


def toGrade(x):
    if x >= 90:
        return "A"
    elif x >= 80 and x < 90:
        return "B"
    elif x >= 70 and x < 80:
        return "C"
    elif x >= 65 and x < 70:
        return "D"
    return "F"


def main():
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    odds = list(filter(filterFunc, nums))
    even = list(filter(lambda t: not filterFunc(t), nums))
    print('odds', odds)
    print('even numbers', even)

    lowers = list(filter(filter2, chars))
    upper = list(filter(lambda t: not filter2(t), chars))
    print(lowers)
    print(upper)

    squares = list(map(sqFunc, nums))
    print(squares)

    letters = list(map(toGrade, grades))
    print(letters)


if __name__ == "__main__":
    main()
