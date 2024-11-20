def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <=6):
        return False

    if not s.isalnum():
        return False

    if not s[0:2].isalpha():
        return False

    is_number = False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0' and not is_number:
                return False
            is_number = True
        elif is_number:
            return False

    return True

main()