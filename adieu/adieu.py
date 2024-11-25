import inflect
p = inflect.engine()

try:
    name_list = []
    while True:
        name = input("Name: ")
        name_list.append(name)

except EOFError:
    mylist = p.join(name_list)
    print(f"Adieu, adieu, to {mylist}")
