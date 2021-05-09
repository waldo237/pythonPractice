def addition(base, *args):
    result = 0
    for arg in args:
        result += arg

    return result


def main():
    print(addition(43,24,65 *87,5456, 23,4,5.5))
    print(addition(43,24,65,87,5456, 23,4,5.5))
    myNums = [5, 10, 15, 20]
    print(addition(*myNums))

if __name__ == "__main__":
    main()
