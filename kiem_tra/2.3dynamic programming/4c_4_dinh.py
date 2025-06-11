import itertools

# Distance matrix
distances = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 5, 'B': 0, 'C': 9, 'D': 10},
    'C': {'A': 6, 'B': 13, 'C': 0, 'D': 12},
    'D': {'A': 8, 'B': 8, 'C': 9, 'D': 0}
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
    print(f"g(B, ∅) = d(B, A) = {distances['B']['A']}")  # 5
    print(f"g(C, ∅) = d(C, A) = {distances['C']['A']}")  # 6
    print(f"g(D, ∅) = d(D, A) = {distances['D']['A']}")  # 8
    print()

    # g(x, {y}) values
    g_B_C = distances['B']['C'] + held_karp('A', 'C', set())
    print(f"g(B, {{C}}) = min(d(B, {{C}}) + g(A, {{}})) = min({distances['B']['C']} + {held_karp('A', 'C', set())}) = {g_B_C}")  # 15

    g_B_D = distances['B']['D'] + held_karp('A', 'D', set())
    print(f"g(B, {{D}}) = min(d(B, {{D}}) + g(A, {{}})) = min({distances['B']['D']} + {held_karp('A', 'D', set())}) = {g_B_D}")  # 18

    g_C_B = distances['C']['B'] + held_karp('A', 'B', set())
    print(f"g(C, {{B}}) = min(d(C, {{B}}) + g(A, {{}})) = min({distances['C']['B']} + {held_karp('A', 'B', set())}) = {g_C_B}")  # 18

    g_C_D = distances['C']['D'] + held_karp('A', 'D', set())
    print(f"g(C, {{D}}) = min(d(C, {{D}}) + g(A, {{}})) = min({distances['C']['D']} + {held_karp('A', 'D', set())}) = {g_C_D}")  # 20

    g_D_B = distances['D']['B'] + held_karp('A', 'B', set())
    print(f"g(D, {{B}}) = min(d(D, {{B}}) + g(A, {{}})) = min({distances['D']['B']} + {held_karp('A', 'B', set())}) = {g_D_B}")  # 13

    g_D_C = distances['D']['C'] + held_karp('A', 'C', set())
    print(f"g(D, {{C}}) = min(d(D, {{C}}) + g(A, {{}})) = min({distances['D']['C']} + {held_karp('A', 'C', set())}) = {g_D_C}")  # 15
    print()

    # g(x, {y, z}) values
    # g(B, {C, D})
    remaining_set = {'C', 'D'}
    d_BC = distances['B']['C']  # 9
    d_BD = distances['B']['D']  # 10
    g_C_D = held_karp('A', 'C', {'D'})  # g(C, {D}) 
    g_D_C = held_karp('A', 'D', {'C'})  # g(D, {C})
    g_B_CD = min(d_BC + g_C_D, d_BD + g_D_C)
    print(f"g(B, {{C, D}}) = min(d(B, {{C}}) + g(C, {{D}}), d(B, {{D}}) + g(D, {{C}}) = min({d_BC} + {g_C_D}, {d_BD} + {g_D_C}) = {g_B_CD}")  # 25

    # g(C, {B, D})
    remaining_set = {'B', 'D'}
    d_CB = distances['C']['B']  # 13
    d_CD = distances['C']['D']  # 12
    g_B_D = held_karp('A', 'B', {'D'})  # g(B, {D})
    g_D_B = held_karp('A', 'D', {'B'})  # g(D, {B})
    g_C_BD = min(d_CB + g_B_D, d_CD + g_D_B)
    print(f"g(C, {{B, D}}) = min(d(C, {{B}}) + g(B, {{D}}), d(C, {{D}}) + g(D, {{B}}) = min({d_CB} + {g_B_D}, {d_CD} + {g_D_B}) = {g_C_BD}")  # 25

    # g(D, {B, C})
    remaining_set = {'B', 'C'}
    d_DB = distances['D']['B']  # 8
    d_DC = distances['D']['C']  # 9
    g_B_C = held_karp('A', 'B', {'C'})  # g(B, {C})
    g_C_B = held_karp('A', 'C', {'B'})  # g(C, {B})
    g_D_BC = min(d_DB + g_B_C, d_DC + g_C_B)
    print(f"g(D, {{B, C}}) = min(d(D, {{B}}) + g(B, {{C}}), d(D, {{C}}) + g(C, {{B}}) = min({d_DB} + {g_B_C}, {d_DC} + {g_C_B}) = {g_D_BC}")  # 23
    print()

    # g(A, {B, C, D}) value
    remaining_set = {'B', 'C', 'D'}
    d_AB = distances['A']['B']  # 10
    g_B_CD = held_karp('A', 'B', {'C', 'D'})  # g(B, {C, D})
    g_C_BD = held_karp('A', 'C', {'B', 'D'})  # g(C, {B, D})
    g_D_BC = held_karp('A', 'D', {'B', 'C'})  # g(D, {B, C})
    g_A_BCD = min(d_AB + g_B_CD, distances['A']['C'] + g_C_BD, distances['A']['D'] + g_D_BC)
    print(f"g(A, {{{', '.join(remaining_set)}}}) = min(d(A, B) + g(B, {{C, D}}), d(A, C) + g(C, {{B, D}}), d(A, D) + g(D, {{B, C}}) = min({d_AB} + {g_B_CD}, {distances['A']['C']} + {g_C_BD}, {distances['A']['D']} + {g_D_BC}) = {g_A_BCD}")  # 35

# Run the program
print_all_held_karp_results()
