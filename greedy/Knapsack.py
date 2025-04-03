import unittest
from bisect import bisect
from itertools import accumulate

def frac_knapsack(vl, wt, w, n):
    """
    Solve the fractional knapsack problem using a greedy algorithm.
    """
    if w < 0 or n < 0:
        return 0
    
    r = sorted(zip(vl, wt), key=lambda x: x[0] / x[1], reverse=True)
    vl, wt = [i[0] for i in r], [i[1] for i in r]
    acc = list(accumulate(wt))
    k = bisect(acc, w)
    
    return (
        0
        if k == 0
        else sum(vl[:k]) + (w - acc[k - 1]) * (vl[k]) / (wt[k])
        if k != n
        else sum(vl[:k])
    )

class TestFractionalKnapsack(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(frac_knapsack([60, 100, 120], [10, 20, 30], 50, 3), 240.0)
    
    def test_case_2(self):
        self.assertEqual(frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 10, 4), 105.0)
    
    def test_case_3(self):
        self.assertEqual(frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 8, 4), 95.0)
    
    def test_case_4(self):
        self.assertEqual(frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 0, 4), 0)
    
    def test_case_5(self):
        self.assertEqual(frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], -8, 4), 0)
    
    def test_case_6(self):
        self.assertEqual(frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 800, 4), 130)
    
    def test_case_7(self):
        with self.assertRaises(TypeError):
            frac_knapsack("ABCD", [5, 4, 6, 3], 8, 400)
    
if __name__ == "__main__":
    unittest.main()