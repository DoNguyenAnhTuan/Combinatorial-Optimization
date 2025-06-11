import itertools

# Define the adjacency matrix for the TSP problem
distances = [
    [0, 5, 8, 4, 5],  # Distances from A
    [5, 0, 7, 4, 5],  # Distances from B
    [8, 7, 0, 8, 6],  # Distances from C
    [4, 4, 8, 0, 8],  # Distances from D
    [5, 5, 6, 8, 0]   # Distances from E
]
# distances = [
#     [0, 4, 9, 5],  # Distances from A
#     [4, 0, 4, 8],  # Distances from B
#     [9, 4, 0, 9],  # Distances from C
#     [5, 8, 9, 0]   # Distances from D
    
# ]
# List of cities (indices)
cities = [0, 1, 2, 3, 4]  # Corresponding to A, B, C, D, E
# cities = [0, 1, 2, 3]  # Corresponding to A, B, C, D


# Initialize results list to store all routes and their costs
results = []

# Generate all permutations of cities (excluding the starting city)
for perm in itertools.permutations(cities[1:]):  # Fix city A (0) as the starting point
    # Form a complete route starting and ending at A
    route = [0] + list(perm) + [0]
    
    # Calculate the total distance of the current route
    current_distance = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
    
    # Add the route and cost to the results
    results.append((route, current_distance))

# Convert numeric path to city labels
city_labels = ['A', 'B', 'C', 'D', 'E']

# Find the minimum distance and corresponding paths
min_distance = min(results, key=lambda x: x[1])[1]
optimal_paths = [route for route, cost in results if cost == min_distance]

# Print all the results
print("STT\tChu trình\t\t\tChi phí")
for index, (route, cost) in enumerate(results, start=1):
    route_labels = ' → '.join(city_labels[i] for i in route)
    print(f"{index}\t{route_labels}\t{cost}")

# Print the conclusion
print("\nKết luận: Chúng ta thấy chu trình có chi phí ngắn nhất là:")
for optimal_route in optimal_paths:
    optimal_route_labels = ' → '.join(city_labels[i] for i in optimal_route)
    print(f"• Chu trình: {optimal_route_labels}")
print(f"• Khoảng cách: {min_distance}")
