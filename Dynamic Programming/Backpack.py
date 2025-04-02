def mf_knapsack(i, wt, val, j):
    global f 
    if f[i][j] < 0:
        if j < wt[i - 1]:
            val = mf_knapsack(i - 1, wt, val, j)
        else:
            val = max(
                mf_knapsack(i - 1, wt, val, j),
                mf_knapsack(i - 1, wt, val, j - wt[i - 1]) + val[i - 1],
            )
        f[i][j] = val
    return f[i][j]


def knapsack(w, wt, val, n):
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w_ in range(1, w + 1):
            if wt[i - 1] <= w_:
                dp[i][w_] = max(val[i - 1] + dp[i - 1][w_ - wt[i - 1]], dp[i - 1][w_])
            else:
                dp[i][w_] = dp[i - 1][w_]

    return dp[n][w_], dp


def knapsack_with_example_solution(w: int, wt: list, val: list):
    if not (isinstance(wt, (list, tuple)) and isinstance(val, (list, tuple))):
        raise ValueError(
            "Both the weights and values vectors must be either lists or tuples"
        )

    num_items = len(wt)
    if num_items != len(val):
        msg = (
            "The number of weights must be the same as the number of values.\n"
            f"But got {num_items} weights and {len(val)} values"
        )
        raise ValueError(msg)
    for i in range(num_items):
        if not isinstance(wt[i], int):
            msg = (
                "All weights must be integers but got weight of "
                f"type {type(wt[i])} at index {i}"
            )
            raise TypeError(msg)

    optimal_val, dp_table = knapsack(w, wt, val, num_items)
    example_optional_set: set = set()
    _construct_solution(dp_table, wt, num_items, w, example_optional_set)

    return optimal_val, example_optional_set


def _construct_solution(dp: list, wt: list, i: int, j: int, optimal_set: set):
    if i > 0 and j > 0:
        if dp[i - 1][j] == dp[i][j]:
            _construct_solution(dp, wt, i - 1, j, optimal_set)
        else:
            optimal_set.add(i)
            _construct_solution(dp, wt, i - 1, j - wt[i - 1], optimal_set)


if __name__ == "__main__":
    val = [3, 2, 4, 4]
    wt = [4, 3, 2, 3]
    n = 4
    w = 6
    f = [[0] * (w + 1)] + [[0] + [-1] * (w + 1) for _ in range(n + 1)]
    optimal_solution, _ = knapsack(w, wt, val, n)
    print(optimal_solution)
    print(mf_knapsack(n, wt, val, w)) 

    optimal_solution, optimal_subset = knapsack_with_example_solution(w, wt, val)
    assert optimal_solution == 8
    assert optimal_subset == {3, 4}
    print("optimal_value = ", optimal_solution)
    print("An optimal subset corresponding to the optimal value", optimal_subset)