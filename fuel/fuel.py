def main():
    print(get_percent("Fraction: "))

def get_percent(prompt):
    while True:
        try:
            X, Y = input(prompt).split('/')
            X, Y = int(X), int(Y)
            per = round((X/Y)*100)
            if X <= Y:
                if per >= 99:
                    return "F"
                elif per <= 1:
                    return "E"
                else:
                    return f"{per}%"
            else:
                pass
        except(ValueError, ZeroDivisionError):
            pass

main()
