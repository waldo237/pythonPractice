import datetime


def perm(l):
    if len(l) <= 1:
        return [l]
    r = []
    for i in range(len(l)):
        s = l[:i] + l[i + 1:]
        p = perm(s)
        for x in p:
            r.append(l[i: i + 1] + x)
    return r


def main():
    evens = [2, 4, 6, 8]
    res = perm(evens)
    name = "Fred"
    print(len("He said his name is {name!r}."))

    today = datetime.date(year=2017, month=1, day=27)
    print(f"{today:%B %d, %Y}")


if __name__ == "__main__":
    main()
