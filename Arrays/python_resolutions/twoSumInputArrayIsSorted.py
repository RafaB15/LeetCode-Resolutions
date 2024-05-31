"""
Given a 1-indexed (when we return indexes, we start in 1) array of integers numbers that is already sorted in non-decreasing order,  
find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    """
    This problem is the same twoSum problem, but now the array is sorted and a condition is enforced for use to use constant
    extra space, so using a dictionary to store the indexes of the numbers is not allowed.
    
    We can solve this problem by putting a pointer to the begginig and the end of the array. We add the numbers upp and if we see
    that the result is larger than the target, then we know that we have to try to decrease it, so we make the index pointing to the end
    be one less, so it points to a smaller number. If the result is smaller than the target, then we know that we have to try to increase it,
    so we make the index pointing to the beginning be one more, so it points to a larger number.
    
    We dp this until we find the two numbers that add up to the target.
    
    Since we will only have two variables, we will be using constant extra space.
    """
    
    l, r = 0, len(numbers) - 1
    
    while l < r:
        sum = numbers[l] + numbers[r]
        
        if sum == target:
            return [l + 1, r + 1]
        elif sum < target:
            l += 1
        else:
            r -= 1
    
    return []
    
# Test cases
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target)) # [1,2]

numbers = [2,3,4]
target = 6
print(twoSum(numbers, target)) # [1,3]

    