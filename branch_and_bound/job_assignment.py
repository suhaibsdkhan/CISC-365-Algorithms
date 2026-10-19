def job_assignment_bnb(cost_matrix):
    from copy import deepcopy

    n = len(cost_matrix)
    U_global = float('inf')
    best_assignment = None

    # Each state: (current_cost, level (worker index), assigned_jobs_set, assignment_so_far)
    P = [(0, 0, set(), [])]

    while P:
        # Choose state with minimum cost so far (l_p)
        min_index = min(range(len(P)), key=lambda i: P[i][0])
        cost_so_far, level, assigned_jobs, assignment = P.pop(min_index)

        # If all workers are assigned, check for global update
        if level == n:
            if cost_so_far < U_global:
                U_global = cost_so_far
                best_assignment = assignment
            continue

        # Expand current state (assign one more job to this worker)
        for job in range(n):
            if job in assigned_jobs:
                continue  # job already taken
            new_cost = cost_so_far + cost_matrix[level][job]

            # Estimate remaining cost (lower bound using greedy min cost)
            unassigned_jobs = set(range(n)) - assigned_jobs - {job}
            est_remaining_cost = 0
            for i in range(level + 1, n):
                est_remaining_cost += min([cost_matrix[i][j] for j in unassigned_jobs]) if unassigned_jobs else 0

            if new_cost + est_remaining_cost >= U_global:
                continue  # prune

            # Add new partial solution to P
            new_assignment = assignment + [(level, job)]
            P.append((new_cost, level + 1, assigned_jobs | {job}, new_assignment))

    return best_assignment, U_global