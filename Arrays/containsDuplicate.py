"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # We create a set
    elements = set()

    # We loop through the list of numbers
    for number in nums:
        # We check if the number is in the set
        if number in elements:
            # If it is, we return True
            return True
        else: 
            # If it's not, we add it to the set
            elements.add(number)
    # If no duplicate is found, we return False
    return False


nums = [1,2,3,5]
print(containsDuplicate(nums)) # True