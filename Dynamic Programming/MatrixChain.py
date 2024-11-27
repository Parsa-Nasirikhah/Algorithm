def mcm(d):
    n = len(d) - 1
    m = {(i, j): float('inf') for i in range(1, n + 1) for j in range(i, n + 1)}
    
    for i in range(1, n + 1):
        m[(i, i)] = 0

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            for k in range(i, j):
                q = m[(i, k)] + m[(k + 1, j)] + d[i - 1] * d[k] * d[j]
                m[(i, j)] = min(m[(i, j)], q)

    return m[(1, n)]

d = [10, 20, 50, 1, 100]
print(mcm(d))
