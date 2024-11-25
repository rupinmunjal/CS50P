from pyfiglet import Figlet
figlet = Figlet()

import sys
import random

def main():

    if len(sys.argv) == 1:
        f = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in figlet.getFonts()):
        f = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    s = input("Input: ")
    figlet.setFont(font=f)
    print(figlet.renderText(s))

main()
