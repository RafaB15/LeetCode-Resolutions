"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    """
    To solve this problem we are going to create an array where each position is the product of all the elements to the left 
    (this can be done in O(n)). Then we will do the same, but to the right. Finally, if we want to know the product of all the elemnets except the 
    one that is in a specific position, we just need to multiplay the elements to the left and right of that position.
    """

    # Initialize a list to store the products of the elements to the left of the current element
    left_products = [1] * len(nums)
    # Initialize a list to store the products of the elements to the right of the current element
    right_products = [1] * len(nums)
    # Create a list to store the final results.
    result = [1] * len(nums)
    #The variables to store the current left or right product to create the arrays start at one, so that the value doesn't affect the multiplication.
    # Create a variable to store the product of the elements to the left of the current element
    left_product = 1
    # Create a variable to store the product of the elements to the right of the current element
    right_product = 1
    # Loop through the list of numbers
    for i in range(len(nums)):
        # Update the left_products list with the product of the elements to the left of the current element
        left_products[i] = left_product
        left_product *= nums[i]
        # Update the right_products list with the product of the elements to the right of the current element
        right_products[len(nums) - i - 1] = right_product
        right_product *= nums[len(nums) - i - 1]
    # Loop through the list of numbers
    for i in range(len(nums)):
        # Update the result list with the product of the elements to the left and right of the current element
        result[i] = left_products[i] * right_products[i]
    # Return the result list
    return result


"""
The previous solution has a time complexity of O(n) and a space complexity of O(n). However, since the array of the solution is what we give back,
it doesn't count towards the space complexity, so if instead of building and multiplying two arrays, we just build everything in the same one,
we get a space complexity of O(1). The time complexity remains the same.
"""

def productExceptSelfSpace(nums):
    result = [1] * len(nums);
    left_product = 1
    right_product = 1

    for i in range(len(nums)):
        result[i] = left_product
        left_product *= nums[i]
    
    for i in range(len(nums)):
        result[len(nums) - i - 1] *= right_product
        right_product *= nums[len(nums) - i - 1]

    """
    También, por estar todo inicializado en 1, lo podríamos hacer así:
    for i in range(len(nums)):
        result[i] *= left_product
        left_product *= nums[i]
        result[len(nums) - i - 1] *= right_product
        right_product *= nums[len(nums) - i - 1]
    """
    
    return result


nums = [1,2,3,4]
print("Space n", productExceptSelf(nums)) # [24,12,8,6]
print("Space 1", productExceptSelfSpace(nums)) # [24,12,8,6]