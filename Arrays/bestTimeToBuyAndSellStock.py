"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # Create a variable to store the maximum profit
    max_profit = 0
    # Create a variable to store the minimum price
    min_price = float('inf')
    # Loop through the list of prices
    for price in prices:
        # Check if the current price is less than the minimum price
        if price < min_price:
            # If it is, update the minimum price
            min_price = price
        # Check if the difference between the current price and the minimum price is greater than the maximum profit
        elif price - min_price > max_profit:
            # If it is, update the maximum profit
            max_profit = price - min_price
    # Return the maximum profit
    return max_profit

#The above solution works because at any given index, you can find what would be the biggest earnings selling that stock that day by substracting
#the minimun value at which it could have been bought in the past.

prices = [7,1,5,3,6,4]
print(maxProfit(prices))

#Brute force
"""
def maxProfit(prices):
    :type prices: List[int]
    :rtype: int
    current_best = 0
    for i in range(len(prices)):
        if  (i == len(prices) - 1):
            return current_best
        
        for j in range(i + 1, len(prices)):
            difference = prices[j] - prices[i]
            if difference > current_best:
                current_best = difference
        
prices = [7,6,4,3,1]
print(maxProfit(prices))
"""