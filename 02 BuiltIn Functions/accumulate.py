

import itertools
def main():
    # accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals, min)
    print(list(acc))

if __name__ == "__main__":
    main()
    