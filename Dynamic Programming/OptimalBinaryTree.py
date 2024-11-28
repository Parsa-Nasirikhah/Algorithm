import sys
from random import randint


class Node:

    def __init__(self, key, freq):
        self.key = key
        self.freq = freq

    def __str__(self):
        return f"Node(key={self.key}, freq={self.freq})"

def print_binary_search_tree(root, key, i, j, parent, is_left):

    if i > j or i < 0 or j > len(root) - 1:
        return

    node = root[i][j]
    if parent == -1:
        print(f"{key[node]} is the root of the binary search tree.")
    elif is_left:
        print(f"{key[node]} is the left child of key {parent}.")
    else:
        print(f"{key[node]} is the right child of key {parent}.")

    print_binary_search_tree(root, key, i, node - 1, key[node], True)
    print_binary_search_tree(root, key, node + 1, j, key[node], False)

def find_optimal_binary_search_tree(nodes):

    nodes.sort(key=lambda node: node.key)

    n = len(nodes)

    keys = [nodes[i].key for i in range(n)]
    freqs = [nodes[i].freq for i in range(n)]

    dp = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]

    total = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]

    root = [[i if i == j else 0 for j in range(n)] for i in range(n)]

    for interval_length in range(2, n + 1):
        for i in range(n - interval_length + 1):
            j = i + interval_length - 1

            dp[i][j] = sys.maxsize
            total[i][j] = total[i][j - 1] + freqs[j]


            for r in range(root[i][j - 1], root[i + 1][j] + 1):  
                left = dp[i][r - 1] if r != i else 0  
                right = dp[r + 1][j] if r != j else 0  
                cost = left + total[i][j] + right

                if dp[i][j] > cost:
                    dp[i][j] = cost
                    root[i][j] = r

    print("Binary search tree nodes:")
    for node in nodes:
        print(node)

    print(f"\nThe cost of optimal BST for given tree nodes is {dp[0][n - 1]}.")
    print_binary_search_tree(root, keys, 0, n - 1, -1, False)


nodes = [Node(i, randint(1, 50)) for i in range(10, 0, -1)]
find_optimal_binary_search_tree(nodes)