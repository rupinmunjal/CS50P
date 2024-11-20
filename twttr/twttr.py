def main():
    string = input("Input: ")
    print(checkVowels(string))

def checkVowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    for char in string:
        if char.lower() in vowels:
            None
        else:
            result += char
    return result

main()