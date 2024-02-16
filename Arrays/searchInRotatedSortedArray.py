"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot 
index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index 
of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    """
    To solve this problem, we have to use an algorithm reminiscent of binary search.
    
    In binary search, when we divided the array in two, we only needed to know if the value
    we were looking for was bigger, smaller or equal to the value in the middle.
    In this case, since the array will be rotated, that will not be enough to know which half of the
    aray to discard.
    
    We have to remember something we used in the minimumInRotatedSubarray exercise, which is 
    that when we choose a pivot to divide the array, one of the halves will be completely ordered.
    This is because the part of the rotated array where the beginning and the end of the original array are
    next to each other will end up in one of the halves, while the other half will be in the right order.
    
    Knowing this, we can use some if statements to know which half look for our target in,
    since when we identify the ordered part, we know that if the target is a number between the beginning and the end
    of this part, then it has to be there if it is in the array.
    """
    # We declare variables for the left and right 
    l = 0
    r = len(nums) - 1

    # We use a while loop to keep looking for the target
    while l <= r:
        # We calculate the middle of the array
        m = (l + r) // 2
        
        # If the middle is the target, we return it
        if nums[m] == target:
            return m

        # Depending on the half of the array that is ordered, we will check 
        # if the target has to be there or could be in the other part.
        if nums[l] <= nums[m]:
            if nums[m] > target and nums[l] <= target:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] < target and nums[r] >= target:
                l = m + 1
            else:
                r = m - 1

    # If we don't find the target, we return -1
    return -1

nums = [4,5,6,7,0,1,2]
target = 1
print(search(nums, target)) # 4

nums = [4,5,6,7,0,1,2]
target = 3
print(search(nums, target)) # -1

nums = [1]
target = 0
print(search(nums, target)) # -1