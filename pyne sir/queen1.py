import networkx as nx
import matplotlib.pyplot as plt

colors = {'R': 'red', 'G': 'green', 'B': 'blue'}

def is_safe(graph, node, color_assignment, color):
    for neighbor in graph[node]:
        if color_assignment[neighbor] == color:
            return False
    return True

def backtrack(graph, node, color_assignment, num_colors, solutions):
    if node == len(graph):
        solutions.append(color_assignment[:])
        return
    for color in list(colors.keys())[:num_colors]:
        if is_safe(graph, node, color_assignment, color):
            color_assignment[node] = color
            backtrack(graph, node + 1, color_assignment, num_colors, solutions)
            color_assignment[node] = None

def graph_coloring(graph, num_colors):
    solutions = []
    color_assignment = [None] * len(graph)
    backtrack(graph, 0, color_assignment, num_colors, solutions)
    return solutions

def find_chromatic_number(graph):
    for num_colors in range(1, len(graph) + 1):
        if graph_coloring(graph, num_colors):
            return num_colors
    return len(graph)

def plot_graph(graph, color_assignment):
    G = nx.Graph()
    for node in graph:
        G.add_node(node)
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    node_colors = [colors[color_assignment[node]] if color_assignment[node] else 'gray' for node in G.nodes()]
    nx.draw(G, with_labels=True, node_color=node_colors, node_size=1000, edge_color='black')
    plt.show()

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

solutions = graph_coloring(graph, len(colors))
print(f"Total colorings: {len(solutions)}")
for sol in solutions:
    print(sol)

chromatic_number = find_chromatic_number(graph)
print(f"Chromatic Number: {chromatic_number}")

if solutions:
    plot_graph(graph, solutions[0])
