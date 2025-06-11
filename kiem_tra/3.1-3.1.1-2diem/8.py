class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(edges, V):
    result = []
    i = 0
    e = 0
    
    edges = sorted(edges, key=lambda item: item.weight)
    
    parent = []
    rank = []
    
    for node in range(V):
        parent.append(node)
        rank.append(0)
    
    while e < V - 1:
        u, v, w = edges[i].u, edges[i].v, edges[i].weight
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        
        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)
    
    return result

# Define the vertices and edges
vertices = 9
edges = [
    Edge(0, 1, 5), Edge(0, 3, 2), Edge(1, 2, 4),
    Edge(1, 3, 3), Edge(1, 4, 5), Edge(2, 4, 6),
    Edge(3, 4, 7), Edge(3, 5, 8), Edge(3, 6, 6),
    Edge(4, 5, 1), Edge(5, 7, 4), Edge(6, 7, 4),
    Edge(7, 8, 2)
]

# Run Kruskal's algorithm
mst = kruskal(edges, vertices)

# Output the result
print("ANH TUẤN - Bài tập 8")
print("Edges in the MST:")
for u, v, weight in mst:
    print(f"{chr(u + 97)} -- {chr(v + 97)} == {weight}")

import networkx as nx
import matplotlib.pyplot as plt

# Tạo đồ thị
G = nx.Graph()

# Thêm các cạnh vào đồ thị
edges = [
    ('a', 'b', 5), ('a', 'd', 2), ('b', 'c', 4),
    ('b', 'd', 3), ('b', 'e', 5), ('b', 'f', 6),
    ('c', 'f', 3), ('d', 'e', 7), ('d', 'g', 6),
    ('d', 'h', 8), ('e', 'f', 1), ('e', 'h', 3),
    ('f', 'i', 4), ('g', 'h', 4), ('h', 'i', 2)
]

G.add_weighted_edges_from(edges)

# Tìm cây khung nhỏ nhất bằng Kruskal
mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

# Vị trí các nút
pos = {
    'a': (0, 2), 'b': (1, 2), 'c': (2, 2),
    'd': (0, 1), 'e': (1, 1), 'f': (2, 1),
    'g': (0, 0), 'h': (1, 0), 'i': (2, 0)
}

# Vẽ toàn bộ đồ thị
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

# Vẽ cây khung nhỏ nhất
nx.draw(mst, pos, with_labels=True, node_color='lightblue', edge_color='red', node_size=500, font_size=10, width=2)

plt.title("Minimum Spanning Tree using Kruskal's Algorithm")
plt.show()