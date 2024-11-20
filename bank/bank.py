def main():
    greeting = input("Greeting: ").lower().strip()
    print(checkGreeting(greeting))

def checkGreeting(greeting):
    if greeting.find("hello") == 0:
        return "$0"
    elif greeting.find("h") == 0:
        return "$20"
    else:
        return "$100"
main()
