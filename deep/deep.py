def checkAnswer(ans):
    if ans == "42" or ans == "forty-two" or ans == "forty two":
        return "Yes"
    else:
        return "No"
def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    print(checkAnswer(ans))

main()
