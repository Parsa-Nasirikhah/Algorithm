import unittest

def count_ways(coins, amount):
    if amount < 0:
        return 0
    
    dp = [1] + [0] * amount
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]

class TestCoinChange(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_ways([1, 2, 5], 5), 4)
    
    def test_case_2(self):
        self.assertEqual(count_ways([2, 3, 7], 7), 2)
    
    def test_case_3(self):
        self.assertEqual(count_ways([3, 5], 8), 1)
    
    def test_case_4(self):
        self.assertEqual(count_ways([1], 0), 1)
    
    def test_case_5(self):
        self.assertEqual(count_ways([2, 4], 3), 0)
    
    def test_case_6(self):
        self.assertEqual(count_ways([], 5), 0)
    
if __name__ == "__main__":
    unittest.main()
