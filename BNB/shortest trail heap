import heapq

def branch_and_bound_shortest_path(graph, start, goal):
    # Each path in the priority queue is (cost_so_far, path)
    P = [(0, [start])]
    U_global = float('inf')  # global upper bound (best known full path cost)
    best_path = None

    while P:
        cost_so_far, path = heapq.heappop(P)
        current = path[-1]

        # If it's a complete solution
        if current == goal:
            if cost_so_far < U_global:
                U_global = cost_so_far
                best_path = path
            continue  # We may still have better options in the queue

        # Expand p
        for neighbor, weight in graph.get(current, []):
            if neighbor in path:
                continue  # avoid cycles
            new_cost = cost_so_far + weight
            if new_cost >= U_global:
                continue  # prune
            new_path = path + [neighbor]
            heapq.heappush(P, (new_cost, new_path))

    return best_path, U_global if best_path else (None, float('inf'))