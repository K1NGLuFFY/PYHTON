import unittest
import pandas as pd
import numpy as np
from bitcoin_simulation import calculate_moving_averages, run_strategy

class TestBitcoinSimulation(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame
        self.dates = pd.date_range(start="2024-01-01", periods=10)
        self.prices = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
        self.df = pd.DataFrame({'Date': self.dates, 'Price': self.prices})

    def test_moving_averages(self):
        # Test MA calculation
        # We need more data for MA7 and MA30
        prices = [10.0] * 30
        df = pd.DataFrame({'Date': pd.date_range(start="2024-01-01", periods=30), 'Price': prices})

        df = calculate_moving_averages(df)

        # Check MA7 at index 6 (7th element)
        self.assertEqual(df.loc[6, 'MA7'], 10.0)
        # Check MA30 at index 29 (30th element)
        self.assertEqual(df.loc[29, 'MA30'], 10.0)

        # Check NaNs
        self.assertTrue(np.isnan(df.loc[5, 'MA7']))
        self.assertTrue(np.isnan(df.loc[28, 'MA30']))

    def test_golden_cross_strategy(self):
        # Construct a scenario where MA7 crosses MA30
        # Let's force MAs by setting prices manually or MAs manually?
        # run_strategy calculates signals based on columns 'MA7' and 'MA30'
        # so we can mock those columns directly.

        dates = pd.date_range(start="2024-01-01", periods=5)
        prices = [100, 100, 100, 100, 100]
        df = pd.DataFrame({'Date': dates, 'Price': prices})

        # Day 0: No prev data
        # Day 1: MA7=9, MA30=10 (OUT -> No action)
        # Day 2: MA7=11, MA30=10 (Cross Over -> BUY)
        # Day 3: MA7=11, MA30=10 (Already IN -> HOLD)
        # Day 4: MA7=9, MA30=10 (Cross Under -> SELL)

        ma7 = [np.nan, 9.0, 11.0, 11.0, 9.0]
        ma30 = [np.nan, 10.0, 10.0, 10.0, 10.0]

        df['MA7'] = ma7
        df['MA30'] = ma30

        ledger = run_strategy(df, initial_cash=100)

        # Check Day 2 (index 1 in 0-indexed iteration logic if we iterate range(len))
        # Wait, the loop is: for i in range(len(df)).
        # i=0: no prev.
        # i=1: prev(i=0) is NaN (ma7[0] is NaN). So logic checks: if not np.isnan(prev_ma30)...
        # ma30[0] is NaN. So condition fails.

        # Let's adjust data so indices align.
        # i=0: skip
        # i=1: prev=0 (valid), curr=1.
        # So we need valid data at index 0.

        ma7 = [9.0, 9.0, 11.0, 11.0, 9.0]
        ma30 = [10.0, 10.0, 10.0, 10.0, 10.0]
        df['MA7'] = ma7
        df['MA30'] = ma30

        ledger = run_strategy(df, initial_cash=100)

        # i=1 (Day 2): prev(0): 9<=10. curr(1): 9<=10. No cross.
        # i=2 (Day 3): prev(1): 9<=10. curr(2): 11>10. Cross! BUY.
        # i=3 (Day 4): prev(2): 11>10. curr(3): 11>10. No cross.
        # i=4 (Day 5): prev(3): 11>10. curr(4): 9<10. Cross! SELL.

        actions = ledger['Action'].tolist()
        self.assertEqual(actions[2], 'BUY')
        self.assertEqual(actions[4], 'SELL')

if __name__ == '__main__':
    unittest.main()
