STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 170.00,
    "AMZN": 190.00,
}


def calculate_portfolio():
    print("\n=== Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(STOCK_PRICES))

    portfolio = {}

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").strip().upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found. Choose one from the available list.")
            continue

        try:
            quantity = float(input(f"Enter quantity of {stock}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    if not portfolio:
        print("No stocks were added.")
        return

    total = 0

    print("\n--- Portfolio Summary ---")
    for stock, quantity in portfolio.items():
        value = STOCK_PRICES[stock] * quantity
        total += value
        print(
            f"{stock}: {quantity:g} shares × "
            f"${STOCK_PRICES[stock]:.2f} = ${value:.2f}"
        )

    print(f"Total investment value: ${total:.2f}")

    save = input("Save result to portfolio.txt? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio.txt", "w", encoding="utf-8") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("=======================\n")
            for stock, quantity in portfolio.items():
                value = STOCK_PRICES[stock] * quantity
                file.write(
                    f"{stock}: {quantity:g} shares = ${value:.2f}\n"
                )
            file.write(f"Total investment value: ${total:.2f}\n")

        print("Portfolio saved to portfolio.txt")


if __name__ == "__main__":
    calculate_portfolio()
