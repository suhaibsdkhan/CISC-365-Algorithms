def minimum_path_sum(grid):
    # grid: 2D list representing the grid of numbers
    
    # m: number of rows in the grid.
    m = len(grid)
    # n: number of columns in the grid.
    n = len(grid[0])
    
    # Create a 2D list dp with dimensions m x n to store the minimum path sum up to each cell.
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the starting cell (top-left corner) with its corresponding grid value.
    dp[0][0] = grid[0][0]
    
    # Fill the first row: each cell can only be reached from the cell on its left.
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    # Fill the first column: each cell can only be reached from the cell above.
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    
    # Fill in the rest of the dp table:
    # Each cell (i, j) can be reached either from the cell above (i-1, j) or the cell to the left (i, j-1).
    # We choose the path with the lower cumulative sum.
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    
    # The bottom-right cell contains the minimum path sum from the top-left to the bottom-right.
    return dp[m - 1][n - 1]