import itertools


def main():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]
    i = iter(days)
    print(next(i))

    with open('dll.py', "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    for m in range(len(days)):
        print(m+1, days[m])
    
    for i, m in enumerate(days, start =1):
        print(i, m)

    for m in zip(days, daysFr):
        print(m[1])

    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, f"{m[1]} means {m[0]} in French")
if __name__ == "__main__":
    main()
