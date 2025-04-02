from __future__ import annotations

import time
from collections.abc import Sequence
from random import randint
import matplotlib.pyplot as plt

def find_max_subarray(
    nums: Sequence[float], start: int, end: int
) -> tuple[int | None, int | None, float]:
    if not nums:
        return None, None, 0
    if start == end:
        return start, end, nums[start]

    mid_point = (start + end) // 2
    left_start, left_end, left_max = find_max_subarray(nums, start, mid_point)
    right_start, right_end, right_max = find_max_subarray(nums, mid_point + 1, end)
    cross_start, cross_end, cross_max = max_crossing_sum(nums, start, mid_point, end)
    
    if left_max >= right_max and left_max >= cross_max:
        return left_start, left_end, left_max
    elif right_max >= left_max and right_max >= cross_max:
        return right_start, right_end, right_max
    return cross_start, cross_end, cross_max

def max_crossing_sum(
    nums: Sequence[float], start: int, mid: int, end: int
) -> tuple[int, int, float]:
    left_max_sum, left_idx = float("-inf"), -1
    right_max_sum, right_idx = float("-inf"), -1
    
    temp_sum = 0
    for i in range(mid, start - 1, -1):
        temp_sum += nums[i]
        if temp_sum > left_max_sum:
            left_max_sum = temp_sum
            left_idx = i
    
    temp_sum = 0
    for i in range(mid + 1, end + 1):
        temp_sum += nums[i]
        if temp_sum > right_max_sum:
            right_max_sum = temp_sum
            right_idx = i
    
    return left_idx, right_idx, (left_max_sum + right_max_sum)

def measure_runtime(size: int) -> float:
    nums = [randint(1, size) for _ in range(size)]
    start_time = time.time()
    find_max_subarray(nums, 0, size - 1)
    return time.time() - start_time

def visualize_performance() -> None:
    sizes = [10, 100, 1000, 10000, 50000, 100000, 200000, 300000, 400000, 500000]
    times = [measure_runtime(size) for size in sizes]
    print("Inputs Count\tExecution Time")
    for size, exec_time in zip(sizes, times):
        print(size, "\t", exec_time)
    
    plt.plot(sizes, times)
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.show()

if __name__ == "__main__":
    from doctest import testmod
    testmod()