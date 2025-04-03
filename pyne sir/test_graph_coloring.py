from graph import Graph

def test_coloring():
    # Create a graph with 4 vertices
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    
    # Find coloring
    colors = g.greedy_coloring()
    print("\nGraph Coloring Result:")
    for vertex in range(g.V):
        print(f"Vertex {vertex} is colored with color {colors[vertex]}")

if __name__ == "__main__":
    print("Testing Graph Coloring Algorithm")
    print("-" * 30)
    test_coloring() 