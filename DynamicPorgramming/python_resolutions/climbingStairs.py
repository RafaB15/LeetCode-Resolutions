"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

    """
    We can solve this problem with dynamic programming, taking into account that, since you can get to step n from step n - 1 and step n - 2,
    then the total amount of different ways that we can get to step n is the sum of the different ways that we can get to step n - 1 and step n - 2.
    """

    preprevious = 0
    previous = 1
    
    for i in range(n):
        current = preprevious + previous
        preprevious = previous
        previous = current
    
    return current