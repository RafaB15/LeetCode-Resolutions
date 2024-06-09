"""
Given a string s, find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    """
    In this solution, we make use of a sliding window to keep track of the longest substring without repeating characters.
    We will check all the biggest substrings that end with each character of the string.
    """
    charSet = set()
    l = 0
    res = 0
    
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    
    return res

# Resolution using a vector to store the maximum of all
def lengthOfLongestSubstringFirstAttempt(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "": return 0
    
    last_appearance = {}
    max_vec = [1] * len(s)
    total_max = 1
    last_appearance[s[0]] = 0


    for i in range(1, len(s)):
        included = False
        if s[i] in last_appearance:
            last_id = last_appearance[s[i]]
            included = (i - 1) - max_vec[i - 1] < last_id 

        max_vec[i] = (max_vec[i - 1] + 1) if not included else i - last_appearance[s[i]]
        total_max = max(total_max, max_vec[i])
        
        last_appearance[s[i]] = i

    return total_max

# Resolution using a variable to store the maximum of all
def lengthOfLongestSubstringSecondAttempt(s):
    """
    :type s: str
    :rtype: int
    """
    
    """
    We solve this problem by keeping track of the last appearance of each character in the string.
    When we encounter a new character we check wheter or not it belongs to the substring that ends with the letter just before it.
    If it does then we take the substring that starts after the last appearance of the character and ends with the current character.
    If it does not then we continue the substring that ends with the last character.
    """
    # Max lenght of the substring that end with the previous character
    prev_max = 0
    # Max lenght of all substrings evaluated
    max_lenght = 0
    # Dictionary for the last appearance of each character
    last_appearance = {}

    # Iterate over the string
    for i in range(len(s)):
        # Check if the character is included in the substring that ends with the previous character
        included = False
        if s[i] in last_appearance:
            included = (i - 1) - prev_max < last_appearance[s[i]]

        # Update the max lenght of the substring that ends with the current character
        current_max = (prev_max + 1) if not included else i - last_appearance[s[i]]
        
        # Update the max lenght of all substrings evaluated
        max_lenght = max(max_lenght, current_max)
        
        # Update the last appearance of the character and the previous max for the nextn iteration
        prev_max = current_max
        last_appearance[s[i]] = i

    # Return the max lenght of all substrings evaluated
    return max_lenght


s = "abcabcbb"
print(lengthOfLongestSubstringSecondAttempt(s))