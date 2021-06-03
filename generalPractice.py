""" itertools.compress() Filters one iterable with another."""
import itertools


# def main():
#     class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah"
#               "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]
#     selections = [True, False, True, False, True]
#     result = itertools.compress(class1, selections)
#     for each in result:
#         print(each, end=" ")


def triangle(row):
    for i in range(row):
        print(' ' * (row-i-1) + '+' * (2 * i + 1))

if __name__ == "__main__":
    triangle(12)
"""        +
          +++
         +++++
        +++++++
       +++++++++
      +++++++++++
     +++++++++++++
    +++++++++++++++
   +++++++++++++++++
  +++++++++++++++++++
 +++++++++++++++++++++
+++++++++++++++++++++++ """