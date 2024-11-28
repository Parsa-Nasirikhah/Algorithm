import math

class Graph:
    def __init__(self, n=0): 
        self.n = n
        self.w = [
            [math.inf for j in range(n)] for i in range(n)
        ] 
        self.dp = [
            [math.inf for j in range(n)] for i in range(n)
        ] 

    def add_edge(self, u, v, w):
 
        self.dp[u][v] = w

    def floyd_warshall(self):

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.dp[i][j] = min(self.dp[i][j], self.dp[i][k] + self.dp[k][j])

    def show_min(self, u, v):
 
        return self.dp[u][v]

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    graph = Graph(5)
    graph.add_edge(0, 2, 9)
    graph.add_edge(0, 4, 10)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 3, 7)
    graph.add_edge(3, 0, 10)
    graph.add_edge(3, 1, 2)
    graph.add_edge(3, 2, 1)
    graph.add_edge(3, 4, 6)
    graph.add_edge(4, 1, 3)
    graph.add_edge(4, 2, 4)
    graph.add_edge(4, 3, 9)
    graph.floyd_warshall()
    print(
        graph.show_min(1, 4)
    ) 
    print(
        graph.show_min(0, 3)
    )