"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    
    """
    We can solve this problem by making a tuple with the amount of characters for each word and then using that 
    as  a key for a hashmap. The value for each key will be a list of strings that have the same amount of characters.
    The complexity of this is O(m * n), where m is the amount of strings and n is the length of the longest string.
    """
    
    res = {}

    for str in strs:
        count = [0] * 26 # 26 letters in the alphabet
        
        for char in str:
            count[ord(char) - ord('a')] += 1
            
        if tuple(count) not in res:
            res[tuple(count)] = []
        res[tuple(count)].append(str)

    return res.values()
        