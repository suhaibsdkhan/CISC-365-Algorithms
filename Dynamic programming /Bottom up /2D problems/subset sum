def subset_sum(arr, target):
    # Get the length of the array
    n = len(arr)
    # Create a 2D list dp with dimensions (n+1) x (target+1),
    # initialized to False
    dp = [[False]*(target+1) for _ in range(n+1)]
    
    # Set dp[i][0] = True for all i, because sum 0 is always achievable
    dp[0][0] = True
    for i in range(1, n+1):
        dp[i][0] = True
    
    # Fill the dp table
    for i in range(1, n+1):
        for j in range(1, target+1):
            # If the current element can be included
            if arr[i-1] <= j:
                # Either include it or exclude it
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                # If it's bigger than j, skip it
                dp[i][j] = dp[i-1][j]
    
    # Return True if target subset sum is found
    return dp[n][target]