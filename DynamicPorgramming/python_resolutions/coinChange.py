"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    
    """
    To solve this problem we will calculate the minimum amount of coins necessary to represent every number from 0 to the requested amount, so that whenever we 
    have to calculate a the minimum for a value, we can try using one coin minus the minimum amount of coins necessary to represent the amount minus the current coins value.
    This is the way we can reutilize the previous calculations.
    This is a simpler algorithm than the knapsack problem in terms of memory usage, because we have an infinite amount of each coin, so that is one less dimension.
    This algorithm is O(n*m) where n is the amount and m is the number of coins, so it is a pseudo-polynomial algorithm.
    The space complexity is O(n) because we only need to store the minimum amount of coins for each amount from 0 to the requested amount.
    """
    # We create a list where for every OPT[n] we store the minimum amount of coins necessary to represent the amount n.
    # We initialize with amount + 1, since the maximum amount of coins necessary to represent the amount is the amount itself.
    OPT = [amount + 1] * (amount + 1)
    OPT[0] = 0

    # We will iterate through every amount from 1 to the requested amount to solve the subproblems
    for i in range(1, amount + 1):
        # We will try using every coin
        for coin in coins:
            # We calculate the rest of the amount
            rest = i - coin
            # If the rest is greater or equal to 0, we can use the previous calculation to calculate the minimum amount of coins necessary to represent the amount
            if rest >= 0:
                # We store the minimum amount of coins necessary to represent the amount thus far
                OPT[i] = min(OPT[i], OPT[rest] + 1)
    
    # If the minimum amount of coins necessary to represent the amount is the amount + 1, we return -1, since it is impossible to represent the amount
    return OPT[amount] if OPT[amount] != (amount + 1) else -1
    

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))