from collections import defaultdict


def main():
    fruits = ['mango', 'peach', 'orange', 'banana',
        'apple', 'grape', 'banana', 'banana', 'mango']

    fruitCounter = defaultdict(int)

    for fruit in fruits:
        fruitCounter[fruit] += 1

    for(k,v) in fruitCounter.items():
        print(f"{k}: {str(v)}")
        
if __name__ == "__main__":
    main()

""" 
mango: 2
peach: 1
orange: 1
banana: 3
apple: 1
grape: 1
 """