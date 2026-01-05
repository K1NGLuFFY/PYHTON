import pandas as pd
import numpy as np

def simulate_bitcoin_price(days=60, initial_price=50000, volatility=0.03, drift=0.0005, seed=42):
    """
    Simulates Bitcoin price data using a geometric random walk.
    """
    np.random.seed(seed)
    returns = np.random.normal(loc=drift, scale=volatility, size=days)
    price_path = [initial_price]
    for r in returns:
        price_path.append(price_path[-1] * (1 + r))

    # Generate dates
    dates = pd.date_range(start="2024-01-01", periods=days+1)

    # Create DataFrame (skipping the initial seed price to just have 'days' worth of movement,
    # or keep it as day 0. Let's keep the generated path.
    # The prompt asks for 60 days of data.
    # If we want exactly 60 rows, we can slice.
    df = pd.DataFrame({'Date': dates, 'Price': price_path})
    return df.iloc[1:].reset_index(drop=True)

def calculate_moving_averages(df):
    """
    Calculates 7-day and 30-day Moving Averages.
    """
    df['MA7'] = df['Price'].rolling(window=7).mean()
    df['MA30'] = df['Price'].rolling(window=30).mean()
    return df

def run_strategy(df, initial_cash=100000):
    """
    Implements the Golden Cross trading algorithm.
    """
    cash = initial_cash
    btc = 0
    position = 'OUT' # Current position: 'IN' (holding BTC) or 'OUT' (holding Cash)

    ledger = []

    for i in range(len(df)):
        price = df.loc[i, 'Price']
        date = df.loc[i, 'Date']
        curr_ma7 = df.loc[i, 'MA7']
        curr_ma30 = df.loc[i, 'MA30']

        action = "HOLD"

        # We need previous day data to determine a crossover
        if i > 0:
            prev_ma7 = df.loc[i-1, 'MA7']
            prev_ma30 = df.loc[i-1, 'MA30']

            # Check if MAs are valid numbers
            if not np.isnan(prev_ma30) and not np.isnan(curr_ma30):
                # Golden Cross: MA7 crosses above MA30
                if prev_ma7 <= prev_ma30 and curr_ma7 > curr_ma30:
                    if position == 'OUT':
                        action = "BUY"
                        btc = cash / price
                        cash = 0
                        position = 'IN'

                # Death Cross: MA7 crosses below MA30
                elif prev_ma7 >= prev_ma30 and curr_ma7 < curr_ma30:
                    if position == 'IN':
                        action = "SELL"
                        cash = btc * price
                        btc = 0
                        position = 'OUT'

        # Calculate current portfolio value
        current_val = cash + (btc * price)

        ledger.append({
            'Day': i + 1,
            'Date': date.strftime('%Y-%m-%d'),
            'Price': round(price, 2),
            'MA7': round(curr_ma7, 2) if not np.isnan(curr_ma7) else None,
            'MA30': round(curr_ma30, 2) if not np.isnan(curr_ma30) else None,
            'Action': action,
            'Portfolio Value': round(current_val, 2)
        })

    return pd.DataFrame(ledger)

if __name__ == "__main__":
    # 1. Simulate Data
    print("Simulating Bitcoin Data...")
    df = simulate_bitcoin_price(days=60)

    # 2. Calculate MAs
    df = calculate_moving_averages(df)

    # 3. Run Strategy
    ledger_df = run_strategy(df)

    # 4. Print Ledger
    print("\nDaily Ledger of Trades:")
    # Set pandas display options to ensure all columns/rows are visible if needed,
    # though with 60 rows it might be long.
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)
    print(ledger_df.to_string(index=False))

    # 5. Final Performance
    initial_val = 100000
    final_val = ledger_df.iloc[-1]['Portfolio Value']
    profit = final_val - initial_val
    roi = (profit / initial_val) * 100

    print(f"\nFinal Portfolio Performance:")
    print(f"Initial Value: ${initial_val:,.2f}")
    print(f"Final Value:   ${final_val:,.2f}")
    print(f"Profit/Loss:   ${profit:,.2f} ({roi:.2f}%)")
