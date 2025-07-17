import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if to_currency in data["rates"]:
            rate = data["rates"][to_currency]
            converted = amount * rate

            print(f"\n💱 {amount} {from_currency} = {converted:.2f} {to_currency}")
            print(f"Exchange Rate: 1 {from_currency} = {rate:.4f} {to_currency}")
            print(f"Last Updated: {data['date']}")
        else:
            print("❌ Currency code not found in response.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")

# Example usage
try:
    amount = float(input("Enter amount: "))
    from_curr = input("From currency (e.g., USD): ").upper()
    to_curr = input("To currency (e.g., EUR): ").upper()
    convert_currency(amount, from_curr, to_curr)

except ValueError:
    print("❌ Please enter a valid number for amount.")
