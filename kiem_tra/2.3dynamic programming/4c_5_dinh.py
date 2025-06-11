import itertools

# Distance matrix for 5 vertices (A, B, C, D, E)
distances = {
    'A': {'A': 0, 'B': 5, 'C': 8, 'D': 4, 'E': 5},
    'B': {'A': 5, 'B': 0, 'C': 7, 'D': 4, 'E': 5},
    'C': {'A': 8, 'B': 7, 'C': 0, 'D': 8, 'E': 6},
    'D': {'A': 4, 'B': 4, 'C': 8, 'D': 0, 'E': 8},
    'E': {'A': 5, 'B': 5, 'C': 6, 'D': 8, 'E': 0},
}

cities = list(distances.keys())  # List of cities

# Function to calculate g(x, S) using the Bellman-Held-Karp formula
def held_karp(start, current, remaining):
    if not remaining:  # If the set is empty
        return distances[current][start]  # Return distance back to the start

    # Find the minimum g value
    min_cost = float('inf')
    for city in remaining:
        new_remaining = remaining - {city}
        cost = distances[current][city] + held_karp(start, city, new_remaining)
        min_cost = min(min_cost, cost)

    return min_cost

# Function to print results for specified cases
def print_all_held_karp_results():
    # g(x, ∅) values
    for city in cities:
        print(f"g({city}, ∅) = d({city}, A) = {distances[city]['A']}")  
    print()

    # g(x, {y}) values
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            current_city = cities[i]
            next_city = cities[j]
            g_value = distances[current_city][next_city] + held_karp('A', next_city, set())
            print(f"g({current_city}, {{{next_city}}}) = min(d({current_city}, {{{next_city}}}) + g(A, {{}})) = min({distances[current_city][next_city]} + {held_karp('A', next_city, set())}) = {g_value}")
    print()

    # g(x, {y, z}) values
    for combination in itertools.combinations(cities[1:], 2):  # Combinations of 2 out of 4 (B, C, D, E)
        for city in cities:
            if city not in combination:  # Calculate g(city, {combination})
                remaining_set = set(combination)
                d_values = [distances[city][c] for c in combination]
                g_comb = [held_karp('A', c, remaining_set - {c}) for c in combination]
                g_value = min(d_values[i] + g_comb[i] for i in range(len(combination)))
                print(f"g({city}, {{{', '.join(combination)}}}) = min(d({city}, {{{', '.join(combination)}}}) + g({', '.join(combination)}, {{}})) = min({', '.join(str(d) + ' + ' + str(g) for d, g in zip(d_values, g_comb))}) = {g_value}")
    print()

    # g(A, {B, C, D, E}) value
    remaining_set = {'B', 'C', 'D', 'E'}
    d_A = distances['A']
    g_values = [
        held_karp('A', 'B', {'C', 'D', 'E'}),
        held_karp('A', 'C', {'B', 'D', 'E'}),
        held_karp('A', 'D', {'B', 'C', 'E'}),
        held_karp('A', 'E', {'B', 'C', 'D'}),
    ]
    g_A_BCDE = min(d_A['B'] + g_values[0], d_A['C'] + g_values[1], d_A['D'] + g_values[2], d_A['E'] + g_values[3])
    print(f"g(A, {{B, C, D, E}}) = min(d(A, B) + g(B, {{C, D, E}}), d(A, C) + g(C, {{B, D, E}}), d(A, D) + g(D, {{B, C, E}}), d(A, E) + g(E, {{B, C, D}}) = min({d_A['B']} + {g_values[0]}, {d_A['C']} + {g_values[1]}, {d_A['D']} + {g_values[2]}, {d_A['E']} + {g_values[3]}) = {g_A_BCDE}")

# Run the program
print_all_held_karp_results()
