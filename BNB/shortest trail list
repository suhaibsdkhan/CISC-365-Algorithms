def branch_and_bound_with_list(graph, start, goal):
    P = [(0, [start])]  # List of tuples: (cost_so_far, path)
    U_global = float('inf')
    best_path = None

    while P:
        # Manually find and remove the path with the smallest cost
        min_index = min(range(len(P)), key=lambda i: P[i][0])
        cost_so_far, path = P.pop(min_index)
        current = path[-1]

        # Check for completion
        if current == goal:
            if cost_so_far < U_global:
                U_global = cost_so_far
                best_path = path
            continue

        # Expand the current path
        for neighbor, weight in graph.get(current, []):
            if neighbor in path:
                continue  # avoid cycles
            new_cost = cost_so_far + weight
            if new_cost >= U_global:
                continue  # prune
            new_path = path + [neighbor]
            P.append((new_cost, new_path))  # add q to P

    return best_path, U_global if best_path else (None, float('inf'))