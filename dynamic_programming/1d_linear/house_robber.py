def robbery(s):
    # s: list of integers representing the money available at each house.
    
    # Initialize variables:
    # n is the total number of houses.
    n = len(s)
    # dp is a list where dp[i] will store the maximum amount that can be robbed from houses 0 to i.
    # We initialize it with zeros.
    dp = [0] * n
    
    # Base case for the first house:
    # The maximum money robbed up to house 0 is simply the money at that house.
    dp[0] = s[0]
    
    # Base case for the second house:
    # The robber can choose either the first house or the second house, so take the maximum.
    dp[1] = max(s[0], s[1])
    
    # Process with dynamic programming for each house from the third one onward.
    # For each house i, we decide whether to:
    #   (a) Skip the current house and keep the maximum value up to the previous house: dp[i - 1], or
    #   (b) Rob the current house and add its value to the maximum up to house i-2: s[i] + dp[i - 2].
    # We take the maximum of these two options.
    for i in range(2, n):
        dp[i] = max(dp[i - 1], s[i] + dp[i - 2])
        
    # The final element in dp (dp[n-1]) holds the maximum money that can be robbed from all houses.
    return dp[n - 1]