import emoji

def emojize(user_input):
    return emoji.emojize(user_input, language="alias")

def main():
    user_input = input("Input: ")
    print(emojize(user_input))

if __name__ == "__main__":
    main()
