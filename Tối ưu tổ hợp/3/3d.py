# Data
# w = [5, 8, 3]  # Weights
# v = [45, 48, 35]  # Values


w = [4,3,2,1]  # Weights
v = [5,4,3,2]  # Values

K = 6  # Capacity
N = [i + 1 for i in range(len(w))]  # Item indices

from docplex.mp.model import Model

# Create model
model = Model(name='Knapsack')

# Variables: x[i] is 1 if item i is included, 0 otherwise
x = {i: model.binary_var(name=f'x_{i}') for i in N}

# Objective: Maximize total value
model.maximize(model.sum(x[i] * v[i - 1] for i in N))

# Constraint: Total weight should not exceed capacity
model.add_constraint(model.sum(x[i] * w[i - 1] for i in N) <= K, 'weight_constraint')

# Solve the model
solution = model.solve()

# Print model information and solution
model.print_information()
if solution:
    model.print_solution()
    
    # Generate x* output
    optimal_solution = [int(x[i].solution_value > 0.5) for i in N]
    # print("Giải tối ưu x* =", tuple(optimal_solution))  # In ra x*
    print("Optimal solution x* =", tuple(optimal_solution))
    
    # Retrieve the value of the objective
    z_star = model.objective_value  # Retrieve the value of the objective
    # print("Giá trị tối đa (z*) =", z_star)
    print("Maximum value (z*) =", z_star)
else:
    # print("Không tìm thấy giải pháp tối ưu.")
    print("No optimal solution found.")
