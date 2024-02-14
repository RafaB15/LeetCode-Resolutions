"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Create a dictionary to store the index of the numbers
    num_dict = {}
    # Loop through the list of numbers
    for i in range(len(nums)):
        # Check if the difference between the target and the current number is in the dictionary
        if target - nums[i] in num_dict:
            # If it is, return the index of the current number and the index of the difference
            return [num_dict[target - nums[i]], i]
        # If the difference is not in the dictionary, add the current number and its index to the dictionary
        num_dict[nums[i]] = i
    # If no solution is found, return an empty list
    return []


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target)) # [0,1]