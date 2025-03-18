def coin_change(coins, amount):
    # Initialize dp array with infinity for all amounts
    dp = [float('inf')] * (amount + 1)
    # Base case: 0 coins needed to make amount 0
    dp[0] = 0
    
    # Process each coin
    for coin in coins:
        # Update dp for all values from coin up to amount
        for x in range(coin, amount + 1):
            # Compare current dp[x] to using this coin (dp[x - coin] + 1)
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    # Return the result or -1 if it is not possible
    return dp[amount] if dp[amount] != float('inf') else -1