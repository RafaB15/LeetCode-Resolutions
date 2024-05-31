"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""
def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    """
    To solve this problem in O(log(n)) time we have to use techniques reminiscent of binary search to halve the 
    array in half in each step and retain only one half. 
    We will decide which half to retain by understanding the problem a little better.
    If a completely sorted array is rotated an n amount of times, now our array has 2 sorted parts,
    divided by a pivot, which is the smallest value in the array.
    When doing binary search, we will take the value in the middle as a posible smallest value and 
    by checking wheter or not it is smaller or higher thatn the left and rightmost values,
    we can know which half to keep looking at and which half to discard.
    """
    # We initialize the res variable where we will store the result
    res = nums[0]
    
    #We create variables for the indexes of the left and right borders
    l, r = 0, len(nums) - 1
    
    while l <= r:
        # If the leftmost value is smaller that the rightmost, that means that the section of
        # the array that we are looking at is sorted, so we can take the leftmost value as our final candidate.
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        # We calculate the middle index
        m = (l + r) // 2
        
        # We check if the middle index is smaller than the value in res, so we won't check this value again
        res = min(res, nums[m])

        # If the value in the middle is bigger than the value in the leftmost index, that means that the left half is sorted
        # else we should look at the right half, but either way, the middle value won't be checked again

        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    
    return res


"""
Primer intento que no sale muy bien
Podemos dividir el vector hasta encontrar un número que sea menor al que va antes


def findMinRecursive(nums, start, end):
    middle = (start + end) // 2
    
    if start == middle:
        return nums[middle]

    if nums[start] >= nums[middle]:
        return findMinRecursive(nums, start, middle)
    elif nums[middle] >= nums[end]:
        return findMinRecursive(nums, middle + 1, end)    
    else:
        return nums[0]

def findMin(nums):

    :type nums: List[int]
    :rtype: int
 
    return findMinRecursive(nums, 0, len(nums) - 1)
"""

nums = [3,4,5,1,2]
print(findMin(nums)) # 1

nums = [4,5,6,7,2]
print(findMin(nums)) # 0