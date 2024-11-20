def main():
    amountDue()

def amountDue():
    change = 50
    while change > 0:
        print(f"Amount Due: {change}")
        money = insertCoin()
        if money in [5, 10, 25]:
            change -= money

    print(f"Change Owed: {abs(change)}")

def insertCoin():
    return int(input("Insert Coin: "))

main()
