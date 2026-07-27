# https://leetcode.com/problems/valid-anagram/description/
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

# { 
#  "j" : 1,
#  "a" : 1,
#  "r" : 1 
# }

# { 
#  "j" : 1,
#  "a" : 1,
#  "m" : 1 
# }

def isAnagram(s: str, t: str) -> bool:
    # { key, value }
    storeS = {}
    storeT = {}

    #{'r': 2, 'a': 2, 'c': 2, 'e': 1}
    for char in s:
        if char not in storeS:
            storeS[char] = 1
        else: 
            storeS[char] += 1

    for char in t:
        if char not in storeT:
            storeT[char] = 1
        else: 
            storeT[char] += 1

    if storeS == storeT:
        return True

    return False


s = "racecar"
t = "carrace"
print(isAnagram(s, t))