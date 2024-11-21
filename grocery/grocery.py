def main():
    get_grocery()

def get_grocery():
    try:
        fruits = []
        while True:
            fruit = input("").upper()
            fruits.append(fruit)

    except EOFError:
        print('\n')
        print_grocery(fruits)

def print_grocery(fruits):
    unique_fruits = set(fruits)
    for fruit in sorted(unique_fruits):
        print(f"{fruits.count(fruit)} {fruit}")

main()
