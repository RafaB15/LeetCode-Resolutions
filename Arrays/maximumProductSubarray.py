"""Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
"""
def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    """
    To solve this problem, we will do something similar to the simpler version that had us adding up the numbers instead of multiplying them.
    Instead of saving only the maximum result including a given element, we will also store the minimum, because if the minimum is negative
    and so is the current number, them being multiplied could result in a bigger number.
    This version uses a vector so the time complexity is O(n) and the space complexity is O(n). There is a simpler version down below.
    """
    min_vector = [0] * len(nums)
    max_vector = [0] * len(nums)

    min_vector[0] = nums[0]
    max_vector[0] = nums[0]

    for i in range(1,len(nums)):
        current_value = nums[i]
        max_vector[i] = max(min_vector[i - 1] * current_value,
                            max_vector[i - 1] * current_value, 
                            current_value)
        min_vector[i] = min(min_vector[i - 1] * current_value,
                            max_vector[i - 1] * current_value,
                            current_value)
        
    return max(max_vector)

def maxProductTwo(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current_max = 1
    current_min = 1
    
    result = float('-inf')
    
    
    for num in nums:
        temp_max = current_max
        current_max = max(temp_max * num, current_min * num, num)
        current_min = min(temp_max * num, current_min * num, num)

        result = max(result, current_max)
    
    return result

nums = [2,3,-2,4, -4]
print(maxProduct(nums)) # 6

nums = [-2,0,-1]
print(maxProduct(nums)) # 0

nums = [-1, -2, -3]
print(maxProduct(nums)) # 6