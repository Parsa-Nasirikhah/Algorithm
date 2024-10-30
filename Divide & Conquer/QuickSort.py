from math import ceil

def partition(array, left, top):
    pvot = array[left]
    i = left + 1
    j = top

    while True:
        while i <= j and array[i] <= pvot:
            i += 1

        while i <= j and array[j] >= pvot:
            j -= 1
        
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break

    array[left], array[j] = array[j], array[left]
    return j


def sort(array, left, top):
    if left < top:
        index = partition(array, left, top)
        sort(array, left, index - 1)
        sort(array, index + 1, top)


mylist = list(map(int, input().strip().split()))
sort(mylist, 0, len(mylist) - 1)
print(" ".join(map(str, mylist)))
