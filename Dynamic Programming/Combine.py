def combine(n: int, k: int):
    indices = list(range(1, k + 1))
    while True:
        yield indices.copy() 
        for i in range(k - 1, -1, -1):
            if indices[i] != i + n - k + 1:
                break
        else:
            return 
        indices[i] += 1
        for j in range(i + 1, k):
            indices[j] = indices[j - 1] + 1

n = 1000
k = 500
for comb in combine(n, k):
    print(comb)
