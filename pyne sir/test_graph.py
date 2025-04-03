import networkx as nx
import matplotlib.pyplot as plt

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
    
    def draw_graph(self, coloring):
        G = nx.Graph()
        for u in self.adj:
            for v in self.adj[u]:
                G.add_edge(u, v)
        color_map = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "gray", "brown", "cyan"]
        node_colors = [color_map[coloring[i] % len(color_map)] for i in range(self.V)]
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=15, edge_color='black')
        plt.show()

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

coloring = g.greedy_coloring()
g.draw_graph(coloring)
