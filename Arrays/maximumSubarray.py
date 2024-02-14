"""
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.
"""
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    """
    In order to solve this problem, we are going to use dynamic programming. 
    We will separate the problem into the subproblems of, given a certain position, what is the largest number that includes it.
    When we advance through the list, we will see if it's better to add the biggest number that includes the last element, 
    or to start from the current element.
    To reconstruct the solution, we will store the position of the biggest number that includes the current element.
    The titme complexity of this solution is O(n) and the space complexity is O(1).
    """
    # Create a variable to store the maximum sum of every subarray that ends with the current element
    local_max = [0] * len(nums);
    # Assing the first element to only itself
    local_max[0] = nums[0];
    # Create a variable to store the maximum sum of every subarray
    max_global = local_max[0];
    # Create a variable to store the position of the biggest number that includes the current element
    max_global_id = 0;

    # Loop through the list of numbers
    for i in range(1, len(nums)):
        # We see if it is convenient to add the last elements or only start from the current one
        local_max[i] = max(local_max[i - 1], 0) + nums[i];
        # We update the maximum sum of every subarray
        if local_max[i] > max_global:
            max_global = local_max[i];
            max_global_id = i;
    return max_global;

nums = [8,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums)) # 6

nums = [1]
print(maxSubArray(nums)) # 1

nums = [5,4,-1,7,8]
print(maxSubArray(nums)) # 23


