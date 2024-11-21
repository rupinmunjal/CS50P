def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    print(outdated(months))

def outdated(months):
    while True:
        try:
            date_input = input("Date: ").title().strip()
            if ',' in date_input:
                date_input = date_input.replace(',','')
                month, date, year = date_input.split(' ')
                month = months.index(month) + 1
            else:
                month, date, year = date_input.split('/')

            if int(date) <= 31 and int(month) <= 12:
                return f"{year}-{str(month).zfill(2)}-{str(date).zfill(2)}"
        except ValueError:
            pass
main()
