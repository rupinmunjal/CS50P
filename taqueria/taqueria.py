def main():
    taqueria = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    get_total(taqueria)

def get_total(taqueria):
        try:
            price = 0
            while True:
                item = input("Item: ").title()
                if item in taqueria:
                    price += taqueria[item]
                    print(f"${price:.2f}")
        except EOFError:
             print('')
main()
