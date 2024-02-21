"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.
"""
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    """
    We can solve this problem by using a dictionary to keep track of the amount of each letter in the string.
    If they are also the same lenght, then we can check if the amount of each letter is the same in both strings.
    
    Another way to solve this is by sorting the strings and comparing them. This involvs sorting which augments complexity depending on the algorithm used.
    """
    
    if len(s) != len(t):
        return False
    
    count = {}

    for char in t:
        count[char] = count.get(char, 0) + 1
    
    for char in s:
        if char in count:
            if count[char] > 0:
                count[char] -= 1
    
    return sum(count.values()) == 0

t = "aacc"
s = "ccac"
print(isAnagram(s, t)) # False