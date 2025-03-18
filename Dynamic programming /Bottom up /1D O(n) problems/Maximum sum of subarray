def max_Subarray(arr):
    # dp[i] will store the maximum subarray sum ending at index i.
    dp = [0] * len(arr)
    
    # Initialize the first element of dp as the first element of arr.
    dp[0] = arr[0]
    
    # Iterate over the array starting from index 1.
    for i in range(1, len(arr)):
        # Either start a new subarray at arr[i] or extend the previous subarray.
        dp[i] = max(arr[i], arr[i] + dp[i - 1])
    
    # The maximum subarray sum is the maximum value in dp.
    return max(dp)