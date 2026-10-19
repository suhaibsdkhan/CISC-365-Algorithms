def longest_common_subsequence(a, b):
    # Get the lengths of the two sequences
    m, n = len(a), len(b)
    # Create a 2D list to store lengths of LCS
    dp = [[0]*(n+1) for _ in range(m+1)]

    # Fill the dp table row by row
    for i in range(1, m+1):
        for j in range(1, n+1):
            # If the characters match, add 1 to the diagonal value
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # Otherwise, take the larger value from top or left
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Return the bottom-right value which is the length of LCS
    return dp[m][n]