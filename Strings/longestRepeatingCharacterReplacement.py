"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase 
English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    
    """
    In this solution, we make use of a sliding window to always have a valid group of characters between l and r.
    We will keep track of the current amount of each letter in the window. In a given window we take the maximum amount of a letter
    and that will be the letter we want to stay the same. The rest of the letters can't be more than k.
    If they are more than k then we will move the window to the right until we have a valid window again.
    The complexity of this solution is O(n), though given that we use max with the dictionary it could be O(26*n), which is still O(n).
    """
    
    # We will keep track of the amount of each letter in the window
    occurences = {}
    # We will store the best result so far here
    res = 0
    # Left pointer
    l = 0
    
    # We make r bigger through each iteration
    for r in range(len(s)):
        # If the letter is already in the dictionary we add one to the amount
        if s[r] in occurences:
            occurences[s[r]] += 1
        # If the letter is not in the dictionary we add it and set the amount to 1
        else:
            occurences[s[r]] = 1
            
        """
        We could also write the last bit like
        occurences[s[r]] = occurences.get(s[r], 0) + 1
        """
        
        # We take the maximum amount of a letter in the window
        max_occurence = max(occurences.values())
        # If the amount of letters that are not the maximum is bigger than k we move the window to the right
        while (r - l + 1) - max_occurence > k:
            occurences[s[l]] -= 1
            l += 1
        # We update the result
        res = max(res, r - l + 1)
    return res



def characterReplacementFirstAttempt(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    
    """
    This method makes use of a sliding window for each letter of the alphabet. 
    It works for many cases, but in large cases it doesn't give the optimal result. Misses by two characters.
    """
    
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'', Z']
    res = 0

    for letter in letters:
        incompatible = 0
        l = 0
        for r in range(len(s)):
            if s[r] != letter:
                incompatible += 1
            
            while incompatible > k and r >= l:
                if s[l] != letter:
                    incompatible -= 1
                l += 1
            
            res = max(res, r - l + 1)
    return res


s = "ABAB"
k = 2

print(characterReplacementFirstAttempt(s, k)) # 4