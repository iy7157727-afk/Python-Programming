import requests

def get_exchange_rates(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if target_currency in data ["rates"]:
        return data ["rates"][target_currency]
    else:
        return None

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rates(base_currency, target_currency)
    if rate:
        return amount * rate
    else:
        return "Invalid Currency Code"

while True:
    print("\nCurrency Converter")
    base = input("Enter the base currency (e.g., USD):").upper()
    target = input("Enter the target currency (e.g., EUR):").upper()

    try:
        amount = float(input("Enter the amount to convert:"))
        result = convert_currency(amount, base, target)
        print(f"{amount} {base} is equal to {result} {target}")
    except ValueError:
        print("Please enter a valid number.")

    again = input("Do you want to convert another currency? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for using the currency converter")
        break
