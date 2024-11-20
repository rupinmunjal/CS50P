def convert(string):
    return string.replace(":)", "🙂").replace(":(", "🙁")

def main():
    user_input = input()
    print(convert(user_input))

main()
