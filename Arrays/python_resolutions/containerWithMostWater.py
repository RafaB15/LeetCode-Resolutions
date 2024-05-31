"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container
"""
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    
    """
    To solve this problem we will have two pointers, one at the beginning of the array and the other at the end of the array.
    We will calculate the area of the current container (between the pointers) and store the maximum area found so far.
    
    After calculating the area, we will move the pointer that has the lowest height. This is because the area of the container
    is limited by the lowest height, so If we moved the bigger height, then the next results are garanteed to be smaller.
    """

    l, r = 0, len(height) - 1
    res = 0
    
    while l < r:
        candidate_answer = min(height[l], height[r]) * (r - l)
        res = max(res, candidate_answer)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return res

def maxAreaBruteForce(height):
    """
    :type height: List[int]
    :rtype: int
    """
    res = 0

    for i, h1 in enumerate(height):
        for j, h2 in enumerate(height[i + 1:], i + 1):
            print(i, j, h1, h2)
            current_w = (j - i) * min(h1, h2)
            print(current_w)
            if current_w > res:
                res = current_w
    return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))  # 49
