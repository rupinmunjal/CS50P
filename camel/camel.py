def main():
    name = input("name: ")
    print(checkCase(name))

def checkCase(name):
    result = ""
    for char in name:
        if(char.isupper()):
            char = "_" + char.lower()
        result += char
    return result

main()
