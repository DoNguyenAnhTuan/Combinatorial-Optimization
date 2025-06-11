import pulp

# Given distance matrix (adjacency matrix)
d = [
    [0, 5, 8, 4, 5],
    [5, 0, 7, 4, 5],
    [8, 7, 0, 8, 6],
    [4, 4, 8, 0, 8],
    [5, 5, 6, 8, 0]
]
n = len(d)  # Number of nodes

# Create the LP problem
prob = pulp.LpProblem("TSP_MTZ_ILP", pulp.LpMinimize)

# Decision variables: x[i][j] is 1 if edge i->j is in the tour, 0 otherwise
x = [[pulp.LpVariable(f"x_{i}_{j}", cat="Binary") for j in range(n)] for i in range(n)]

# Auxiliary variables for the MTZ constraints
u = [pulp.LpVariable(f"u_{i}", lowBound=0, upBound=n-1, cat="Continuous") for i in range(n)]

# Objective function: Minimize the total travel distance
prob += pulp.lpSum(d[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Each node must have exactly one outgoing edge
for i in range(n):
    prob += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1

# Each node must have exactly one incoming edge
for j in range(n):
    prob += pulp.lpSum(x[i][j] for i in range(n) if i != j) == 1

# MTZ constraints to eliminate subtours
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[i][j] <= n - 1

# Solve the problem
prob.solve()

# Get the results
tour_edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i][j]) == 1]
total_distance = pulp.value(prob.objective)

# Build the tour in the required format
tour_string = ""
current_node = 0
mapping = ['A', 'B', 'C', 'D', 'E']  # Mapping from numbers to letters
for _ in range(n):
    for i, j in tour_edges:
        if i == current_node:
            tour_string += f"{mapping[i]}->"
            current_node = j
            break

# Remove the last '->' and add the total distance
tour_string = tour_string[:-2] + f" => z*={total_distance}"

# Output the formatted tour
print(tour_string)
