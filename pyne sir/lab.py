import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, w):
        self.adj[u].append((w, v))
        self.adj[v].append((w, u))

    def prim_mst(self):
        mst = []
        visited = set()
        min_heap = [(0, 0, -1)]
        while min_heap and len(visited) < self.V:
            w, u, parent = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            if parent != -1:
                mst.append((parent, u, w))
            for edge in self.adj[u]:
                if edge[1] not in visited:
                    heapq.heappush(min_heap, (edge[0], edge[1], u))
        return mst

class KruskalGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    def kruskal_mst(self):
        self.edges.sort()
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        mst = []
        for w, u, v in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            if root_u != root_v:
                mst.append((u, v, w))
                self.union(parent, rank, root_u, root_v)
        return mst
