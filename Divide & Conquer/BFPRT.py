from math import ceil


def partition(arr, left, top):
    pvot = arr[top] 
    i = left - 1
    
    for item in range(left, top):
        if arr[item] <= pvot:
            i = i + 1
            arr[i], arr[item] = arr[item], arr[i]
    
    arr[i + 1], arr[top] = arr[top], arr[i + 1]
    return i + 1



def select(arr, low, top, k):
    index = partition(arr, low, top)
    
    if index > k - 1:
        return select(arr, low, index - 1, k)
    
    elif index == k - 1:
        return arr[index]
    
    else:
        return select(arr, index + 1, top, k)



arr = list(map(int, input().split()))
k = int(input())

result = select(arr, 0, len(arr) - 1, k)
print(result)