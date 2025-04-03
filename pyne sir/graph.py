class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def greedy_coloring(self):
        result = [-1] * self.V
        result[0] = 0
        available = [False] * self.V
        for u in range(1, self.V):
            for neighbor in self.adj[u]:
                if result[neighbor] != -1:
                    available[result[neighbor]] = True
            cr = 0
            while cr < self.V and available[cr]:
                cr += 1
            result[u] = cr
            for neighbor in self.adj[u]:
                if result[neighbor] != -1:
                    available[result[neighbor]] = False
        return result
