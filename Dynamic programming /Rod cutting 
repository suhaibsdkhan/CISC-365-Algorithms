import math

# Define the function 'CutRod' to compute the maximum revenue obtainable
# by cutting a rod of length 'n' given the price table 'p'.
def CutRod(p, n):
    # r[j] will hold the best revenue possible for a rod of length j (0 <= j <= n).
    r = [0] * (n + 1)
    # s[j] will hold the length of the first piece to cut off to achieve r[j].
    s = [0] * (n + 1)

    # Loop over each rod length from 1 to n.
    for j in range(1, n + 1):
        
        # Initialize the maximum revenue for rod length j to negative infinity.
        current_max = float('-inf')
        
        # Evaluate all possible first cut positions from 1 to j.
        for i in range(1, j + 1):
            
            # If cutting the rod at length i yields a higher revenue than the current maximum,
            # update the current maximum and record the cut length.
            if current_max < p[i] + r[j - i]:
                current_max = p[i] + r[j - i]
                s[j] = i  # Store the first cut length that gives highest revenue.
                
        # After testing all cuts, record the maximum revenue for rod length j.
        r[j] = current_max

    # Return the maximum revenue for the full rod (length n) and the first cut to make.
    return r[n], s[n]