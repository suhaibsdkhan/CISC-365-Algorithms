def unbounded_knapsack(W, weights, values, n):
    # W: maximum weight capacity of the knapsack
    # weights: list of weights for each item
    # values: list of values for each item
    # n: number of items
    
    # Create a dp list where dp[i] will store the maximum value for capacity i.
    dp = [0] * (W + 1)
    
    # Process all capacities from 0 to W.
    for i in range(W + 1):
        # Try every item for the current capacity.
        for j in range(n):
            # Check if the current item can fit in capacity i.
            if weights[j] <= i:
                # Update dp[i] to the max of its current value or the value
                # obtained by adding the current item's value to the best value for remaining capacity.
                dp[i] = max(dp[i], dp[i - weights[j]] + values[j])
    
    # The maximum value obtainable for capacity W is stored in dp[W].
    return dp[W]