from collections import Counter


def main():
    # list of students in class 1
    class1 = ["Bob", "James", "Chad", "James", "Darcy", "Penny", "Hannah"
              "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy", "Ziggy"]

    c1 = Counter(class1)
    c2 = Counter(class2)

    print(c1["James"])

    print(sum(c1.values()), 'students in class 1')
    print(sum(c2.values()), 'students in class 2')
    c1.update(class2)
    print(sum(c1.values()), "students in class 1 and 2")
    print(c1.most_common())
    print(c1 & c2)

if __name__ == "__main__":
    main()
