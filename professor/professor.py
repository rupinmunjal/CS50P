import random

def main():
    level = get_level()

    score = 0
    for i in range(10):
        X, Y = generate_integer(level)
        sum = X + Y

        user_input = int(input(f"{X} + {Y} = "))
        for j in range(3):
            if user_input == sum:
                score += 1
                break
            elif j == 2:
                print("EEE")
                print(f"{X} + {Y} = {sum}")
            else:
                print("EEE")
                user_input = int(input(f"{X} + {Y} = "))

    print(score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except:
            pass

def generate_integer(level):
    if level == 1:
        X = random.randint(0, 10)
        Y = random.randint(0, 10)
    elif level == 2:
        X = random.randint(10, 100)
        Y = random.randint(10, 100)
    else:
        X = random.randint(100, 1000)
        Y = random.randint(100, 1000)
    return X, Y

if __name__ == "__main__":
    main()
