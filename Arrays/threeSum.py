def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    """
    To solve this problem we will first sort the array, to help us deal with duplicate solutions without the need for a set.
    We first take the first element of the three and we know that if the element's value is a, then the sum of the next two elements
    has to be -a. With this in mind, we can reduce the rest of the problem of finding suitable pairs of numbers to the twoSum problem.
    Furthermore, given that the array is sorted, we can use the variant of the solution that doesn't requiere a dictionary.
    
    The time complexity of this solution is O(n^2), since we have to loop through the array and for each element we have to loop 
    through the rest of the array.
    Sorting the array has a time complexity of O(n log n), so it doesn't affect the overall time complexity.
    """
    
    res = []
    nums.sort()
    
    for i, a in enumerate(nums):
        # We check if the last value we evaluated is the same as the current one, to avoid duplicate solutions
        if i > 0 and a == nums[i - 1]:
            continue
        
        # We declare the pointers for the twoSum problem
        l, r = i + 1, len(nums) - 1
        
        # We loop through the array to find the pairs of numbers that add up to -a
        while l < r:
            
            sum = a + nums[l] + nums[r]
            
            if sum < 0:
                l += 1           
            elif sum > 0:
                r -= 1
            else:
                # If we find a solution, we add it to the result
                res.append([a, nums[l], nums[r]])
                # We update the left pointer to search for more combinations
                l += 1
                # We check if the next number is the same as the current one, to avoid duplicate solutions
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                    
    return res
    


def threeSumIntento(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    """
    Solución sobrecomplicada que no funciona, pues da resultados repetidos. Lo intenté arreglar con sets pero se hizo un quilombo.
    """

    pairs = {}

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if sum not in pairs:
                pairs[sum] = set()
            pairs[sum].add(frozenset({i,j}))

    res = []

    for i in range(len(nums)):
        opposite = -1 * nums[i]
        if opposite in pairs:
            for pair in pairs[opposite]:
                if i not in pair:
                    pair_to_add = list(pair)
                    res.append([nums[pair_to_add[0]], nums[pair_to_add[1]], nums[i]])

    return res    

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums)) # [[-1,-1,2],[-1,0,1]]