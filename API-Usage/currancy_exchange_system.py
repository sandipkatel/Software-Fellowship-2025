import requests
from datetime import datetime

class CurrencyConverter:
    def __init__(self):
        self.base_url = "https://api.exchangerate-api.com/v4/latest"
        self.popular_currencies = {
            'USD': 'US Dollar',
            'EUR': 'Euro',
            'JPY': 'Japanese Yen',
            'NPR': 'Nepalese Rupee',
            'CNY': 'Chinese Yuan',
            'INR': 'Indian Rupee',
            'KRW': 'South Korean Won'
        }
    
    def get_exchange_rates(self, base_currency='USD'):
        """Get current exchange rates for a base currency"""
        url = f"{self.base_url}/{base_currency}"
        
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Error fetching rates: {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
    
    def convert_currency(self, amount, from_currency, to_currency):
        """Convert amount from one currency to another"""
        # Get rates with from_currency as base
        rates_data = self.get_exchange_rates(from_currency)
        
        if rates_data:
            if to_currency in rates_data['rates']:
                rate = rates_data['rates'][to_currency]
                converted_amount = amount * rate
                
                print(f"\n💱 Currency Conversion")
                print(f"Amount: {amount:,.2f} {from_currency}")
                print(f"Exchange Rate: 1 {from_currency} = {rate:.4f} {to_currency}")
                print(f"Converted: {converted_amount:,.2f} {to_currency}")
                print(f"Last Updated: {rates_data['date']}")
                
                return converted_amount
            else:
                print(f"Currency {to_currency} not found.")
                return None
        else:
            print("Could not fetch exchange rates.")
            return None
    
    def show_popular_rates(self, base_currency='USD'):
        """Show exchange rates for popular currencies"""
        rates_data = self.get_exchange_rates(base_currency)
        
        if rates_data:
            print(f"\n🌍 Current Exchange Rates (Base: {base_currency})")
            print(f"Last Updated: {rates_data['date']}")
            print("-" * 45)
            
            for currency, name in self.popular_currencies.items():
                if currency != base_currency and currency in rates_data['rates']:
                    rate = rates_data['rates'][currency]
                    print(f"1 {base_currency} = {rate:8.4f} {currency} ({name})")
    
    def currency_calculator(self):
        """Interactive currency calculator"""
        print("\n🧮 Currency Calculator")
        
        try:
            amount = float(input("Enter amount: "))
            from_curr = input("From currency (e.g., USD): ").upper()
            to_curr = input("To currency (e.g., EUR): ").upper()
            
            if len(from_curr) == 3 and len(to_curr) == 3:
                self.convert_currency(amount, from_curr, to_curr)
            else:
                print("Please enter valid 3-letter currency codes.")
                
        except ValueError:
            print("Please enter a valid amount.")
    
    def run(self):
        """Main program loop"""
        print("💰 Welcome to Currency Exchange Rate Converter!")
        
        while True:
            print("\n" + "="*50)
            print("Choose an option:")
            print("1. Convert currency")
            print("2. Show popular exchange rates")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == '1':
                self.currency_calculator()
                
            elif choice == '2':
                base = input("Enter base currency (default USD): ").upper() or 'USD'
                self.show_popular_rates(base)
                    
            elif choice == '3':
                print("Thank you for using Currency Converter! 💸")
                break
                
            else:
                print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.run()