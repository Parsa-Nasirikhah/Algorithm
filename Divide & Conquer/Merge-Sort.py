from __future__ import annotations

def merge_arrays(left_part: list, right_part: list) -> list:
    merged_result = [None] * (len(left_part) + len(right_part))
    left_idx, right_idx, merge_idx = 0, 0, 0
    
    while left_idx < len(left_part) and right_idx < len(right_part):
        if left_part[left_idx] < right_part[right_idx]:
            merged_result[merge_idx] = left_part[left_idx]
            left_idx += 1
        else:
            merged_result[merge_idx] = right_part[right_idx]
            right_idx += 1
        merge_idx += 1
    
    while left_idx < len(left_part):
        merged_result[merge_idx] = left_part[left_idx]
        left_idx += 1
        merge_idx += 1
    
    while right_idx < len(right_part):
        merged_result[merge_idx] = right_part[right_idx]
        right_idx += 1
        merge_idx += 1
    
    return merged_result

def merge_sort_recursive(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    
    mid_index = len(arr) // 2
    left_sorted = merge_sort_recursive(arr[:mid_index])
    right_sorted = merge_sort_recursive(arr[mid_index:])
    
    return merge_arrays(left_sorted, right_sorted)

if __name__ == "__main__":
    import doctest
    doctest.testmod()