import requests
import sys

def main():
    bitcoin_usd = get_bitcoin()
    user_input = get_user_input()
    amount = bitcoin_usd * user_input

    print(f"${amount:,.4f}")

def get_bitcoin():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response_json = response.json()
    bitcoin_usd = response_json["bpi"]["USD"]["rate_float"]
    return bitcoin_usd

def get_user_input():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        if sys.argv[1].isalpha() == True:
            sys.exit("Command-line argument is not a number")
        else:
            return float(sys.argv[1])


if __name__ == "__main__":
    main()
