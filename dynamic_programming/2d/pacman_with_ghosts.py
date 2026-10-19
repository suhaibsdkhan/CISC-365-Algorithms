def pacman_with_ghosts(ghost):
    m = len(ghost)  # Number of rows
    n = len(ghost[0])  # Number of columns
    dp = [[0] * n for _ in range(m)]
    
    # Base Case: Starting position
    if ghost[0][0] == 1:
        return 0  # If Pacman is blocked at the start
    dp[0][0] = 1
    
    # Fill the first row (only from left)
    for j in range(1, n):
        if ghost[0][j] == 0:
            dp[0][j] = dp[0][j-1]
    
    # Fill the first column (only from above)
    for i in range(1, m):
        if ghost[i][0] == 0:
            dp[i][0] = dp[i-1][0]
    
    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            if ghost[i][j] == 1:
                dp[i][j] = 0  # Blocked by a ghost
            else:
                dp[i][j] = (1 - ghost[i][j-1]) * dp[i][j-1] + (1 - ghost[i-1][j]) * dp[i-1][j]
    
    return dp[m-1][n-1]  # Number of paths to reach cherries

# Example ghost matrix
ghost_matrix = [
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print("Total paths to cherries (Bottom-Up DP):", pacman_with_ghosts(ghost_matrix))