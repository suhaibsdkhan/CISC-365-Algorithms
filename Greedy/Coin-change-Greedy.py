def coin_change(m, coins):
    """
    Returns the minimum number of coins needed to make change for amount m using a greedy algorithm.
    
    If it is not possible to make exact change with the given coins, returns None.
    Note: The greedy algorithm does not always yield the optimal solution.
    
    Parameters:
        m (int): The total amount to make change for.
        coins (list): A list of coin denominations (assumed to be positive integers).
    
    Returns:
        int or None: The count of coins used or None if change cannot be made.
    """
    count = 0
    r = m  # remaining amount
    while r > 0:
        max_coin = 0
        for coin in coins:
            if coin > max_coin and coin <= r:
                max_coin = coin
        if max_coin == 0:
            # No coin can be found to reduce the remaining amount.
            return None
        r -= max_coin
        count += 1
    return count

# Example usage:
if __name__ == "__main__":
    amount = 63
    coin_denominations = [1, 5, 10, 25]
    result = coin_change(amount, coin_denominations)
    if result is not None:
        print(f"Minimum coins needed for {amount} are {result}.")
    else:
        print(f"Cannot make change for {amount} with coins {coin_denominations}.")