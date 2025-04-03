import unittest

def find_minimum_change(denominations: list[int], value: int) -> list[int]:
    """
    Find the minimum change from the given denominations and value
    """
    if value <= 0:
        return []
    
    denominations.sort(reverse=True)  # Ensure the denominations are sorted in descending order
    answer = []
    
    for denomination in denominations:
        while value >= denomination:
            value -= denomination
            answer.append(denomination)
    
    return answer

class TestFindMinimumChange(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_minimum_change([1, 5, 10, 20, 50, 100, 200, 500, 1000,2000], 18745),
                         [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 500, 200, 20, 20, 5])
    
    def test_case_2(self):
        self.assertEqual(find_minimum_change([1, 2, 5, 10, 20, 50, 100, 500, 2000], 987),
                         [500, 100, 100, 100, 100, 50, 20, 10, 5, 2])
    
    def test_case_3(self):
        self.assertEqual(find_minimum_change([1, 2, 5, 10, 20, 50, 100, 500, 2000], 0), [])
    
    def test_case_4(self):
        self.assertEqual(find_minimum_change([1, 2, 5, 10, 20, 50, 100, 500, 2000], -98), [])
    
    def test_case_5(self):
        self.assertEqual(find_minimum_change([1, 5, 100, 500, 1000], 456),
                         [100, 100, 100, 100, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1])
    
if __name__ == "__main__":
    unittest.main()
