# Cấu trúc để lưu trữ đồ thị
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Tìm nút cha gốc (path compression)
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

# Kruskal's algorithm
def kruskal(vertices, edges):
    # Sort edges by weight (trọng số)
    edges.sort(key=lambda x: x[0])

    mst = []  # Lưu các cạnh được chọn vào MST
    ds = DisjointSet(vertices)

    print("Step-by-step edge selection:")
    for weight, edge in edges:
        v1, v2 = edge
        if ds.find(v1) != ds.find(v2):
            ds.union(v1, v2)
            mst.append(edge)
            print(f"Edge {edge} with weight {weight} selected")
        else:
            print(f"Edge {edge} with weight {weight} skipped (creates a cycle)")

    return mst

# Danh sách các cạnh và trọng số của chúng
edges = [
    (1, 'EF'), (2, 'HI'), (2, 'AD'), (3, 'EH'), (3, 'CF'), (3, 'BD'),
    (4, 'BC'), (4, 'GH'), (4, 'FI'), (4, 'HF'), (5, 'AB'), (5, 'BE'),
    (6, 'DG'), (6, 'FB'), (7, 'DE'), (8, 'DH')
]

# Chuyển đổi cạnh dạng chuỗi thành tuple (vì mỗi cạnh có hai đỉnh)
edges = [(w, (e[0], e[1])) for w, e in edges]

# Tập hợp các đỉnh (vertices) trong đồ thị
vertices = set()
for _, edge in edges:
    vertices.update(edge)

# Chạy thuật toán Kruskal
mst = kruskal(vertices, edges)

print("\nMinimum Spanning Tree (MST):", mst)
