import unittest

def minimum_waiting_time(queries: list[int]) -> int:
    """
    This function takes a list of query times and returns the minimum waiting time
    for all queries to be completed.

    Args:
        queries: A list of queries measured in picoseconds

    Returns:
        total_waiting_time: Minimum waiting time measured in picoseconds
    """
    n = len(queries)
    if n in (0, 1):
        return 0
    return sum(query * (n - i - 1) for i, query in enumerate(sorted(queries)))

class TestMinimumWaitingTime(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minimum_waiting_time([3, 2, 1, 2, 6]), 17)
    
    def test_case_2(self):
        self.assertEqual(minimum_waiting_time([3, 2, 1]), 4)
    
    def test_case_3(self):
        self.assertEqual(minimum_waiting_time([1, 2, 3, 4]), 10)
    
    def test_case_4(self):
        self.assertEqual(minimum_waiting_time([5, 5, 5, 5]), 30)
    
    def test_case_5(self):
        self.assertEqual(minimum_waiting_time([]), 0)
    
if __name__ == "__main__":
    unittest.main()