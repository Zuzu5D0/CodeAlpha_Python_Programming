#Task 2:Stock Portfolio tracker
import requests # type: ignore
import json

# Alpha Vantage API key
API_KEY = '58YW04IBZUGXNLBS'

#Stock symbols: AAPL,GOOGL,MSFT,TSLA,AMZN

# Base URL for Alpha Vantage API
BASE_URL = 'https://www.alphavantage.co/query'

# Function to get stock data from Alpha Vantage
def get_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if 'Time Series (Daily)' in data:
        return data['Time Series (Daily)']
    else:
        print("Error fetching data. Please check the stock symbol or API key.")
        return None

# Function to display stock information
def display_stock_info(stock_data, symbol):
    if stock_data:
        print(f"\nStock information for {symbol}:")
        latest_date = list(stock_data.keys())[0]
        latest_data = stock_data[latest_date]
        print(f"Date: {latest_date}")
        print(f"Open: {latest_data['1. open']}")
        print(f"High: {latest_data['2. high']}")
        print(f"Low: {latest_data['3. low']}")
        print(f"Close: {latest_data['4. close']}")
        print(f"Volume: {latest_data['5. volume']}")
    else:
        print("No data available.")

# Portfolio management class
class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if self.stocks[symbol] > quantity:
                self.stocks[symbol] -= quantity
            elif self.stocks[symbol] == quantity:
                del self.stocks[symbol]
            else:
                print("Error: Not enough quantity to remove.")
        else:
            print("Error: Stock not found in portfolio.")

    def track_performance(self):
        for symbol, quantity in self.stocks.items():
            print(f"\nTracking {symbol}:")
            stock_data = get_stock_data(symbol)
            display_stock_info(stock_data, symbol)

def main():
    portfolio = Portfolio()
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Track performance")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
            print(f"Added {quantity} of {symbol} to portfolio.")
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
            print(f"Removed {quantity} of {symbol} from portfolio.")
        elif choice == '3':
            portfolio.track_performance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()


#output:
'''
Stock Portfolio Tracker
1. Add stock
2. Remove stock
3. Track performance
4. Exit
Enter your choice: 1   
Enter stock symbol: AAPL
Enter quantity: 10
Added 10 of AAPL to portfolio.

Stock Portfolio Tracker
1. Add stock
2. Remove stock
3. Track performance
4. Exit
Enter your choice: 1
Enter stock symbol: GOOGL
Enter quantity: 20
Added 20 of GOOGL to portfolio.

Stock Portfolio Tracker
1. Add stock
2. Remove stock
3. Track performance
4. Exit
Enter your choice: 1
Enter stock symbol: AAPL
Enter quantity: 20
Added 20 of AAPL to portfolio.

Stock Portfolio Tracker
1. Add stock
2. Remove stock
3. Track performance
4. Exit
Enter your choice: 1
Enter stock symbol: MSFT
Enter quantity: 30
Added 30 of MSFT to portfolio.

Stock Portfolio Tracker
1. Add stock
2. Remove stock
3. Track performance
4. Exit
Enter your choice: 2
Enter stock symbol: AAPL
Enter quantity: 20
Removed 20 of AAPL from portfolio.

Stock Portfolio Tracker
1. Add stock
2. Remove stock
3. Track performance
4. Exit
Enter your choice: 3

Tracking AAPL:

Stock information for AAPL:
Date: 2024-09-06
Open: 223.9500
High: 225.2400
Low: 219.7700
Close: 220.8200
Volume: 48423011

Tracking GOOGL:

Stock information for GOOGL:
Date: 2024-09-06
Open: 157.3000
High: 157.8300
Low: 150.5500
Close: 150.9200
Volume: 37912130

Tracking MSFT:

Stock information for MSFT:
Date: 2024-09-06
Open: 409.0600
High: 410.6500
Low: 400.8000
Close: 401.7000
Volume: 19609526

Stock Portfolio Tracker
1. Add stock
2. Remove stock
3. Track performance
4. Exit
Enter your choice: 4
Exiting...
'''
