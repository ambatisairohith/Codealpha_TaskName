class StockPortfolio:
    def __init__(self):
        self.portfolio = []  # List to hold stock data

    def add_stock(self, stock, quantity, purchase_price):
        # Add a stock to the portfolio
        self.portfolio.append({
            'Stock': stock,
            'Quantity': quantity,
            'Purchase Price': purchase_price
        })
        print(f"Added {quantity} shares of {stock} at ${purchase_price:.2f} each.")

    def remove_stock(self, stock):
        # Remove a stock from the portfolio
        for item in self.portfolio:
            if item['Stock'].upper() == stock.upper():
                self.portfolio.remove(item)
                print(f"Removed {stock} from the portfolio.")
                return
        print(f"{stock} not found in the portfolio.")

    def view_portfolio(self):
        # Display the current portfolio
        if not self.portfolio:
            print("\nYour portfolio is empty.")
            return
        
        print("\nYour Stock Portfolio:")
        for item in self.portfolio:
            print(f"Stock: {item['Stock']}, Quantity: {item['Quantity']}, Purchase Price: ${item['Purchase Price']:.2f}")

    def get_current_price(self, stock):
        # Manually input current prices for demonstration
        prices = {
            'AAPL': 150.00,
            'GOOGL': 2800.00,
            'AMZN': 3400.00,
            'MSFT': 300.00,
            'TSLA': 700.00
        }
        return prices.get(stock.upper(), None)

    def portfolio_value(self):
        # Calculate the total value of the portfolio
        total_value = 0
        for item in self.portfolio:
            current_price = self.get_current_price(item['Stock'])
            if current_price is not None:
                total_value += current_price * item['Quantity']
            else:
                print(f"Current price for {item['Stock']} not found.")
        return total_value

def main():
    tracker = StockPortfolio()
    
    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Check Portfolio Value")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            stock = input("Enter stock symbol (e.g., AAPL, GOOGL): ")
            quantity = int(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price: "))
            tracker.add_stock(stock, quantity, purchase_price)
        elif choice == '2':
            stock = input("Enter stock symbol to remove: ")
            tracker.remove_stock(stock)
        elif choice == '3':
            tracker.view_portfolio()
        elif choice == '4':
            total_value = tracker.portfolio_value()
            print(f"Total Portfolio Value: ${total_value:.2f}")
        elif choice == '5':
            print("Exiting the tracker.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()