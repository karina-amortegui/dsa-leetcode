from typing import List
from collections import defaultdict

# Group Anagrams 

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"] time complexity:
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]

# Example 3:
# Input: strs = [""]
# Output: [[""]]

# Constraints:
# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

# myHashmap = defaultdict(list)
# myHashmap["{a:1, c:1, t:1}"] = ["act", "cat"]

# O(n * m) n = number of strings m = the number of characters in each string 
def groupAnagrams(strs: List[str]) -> List[List[str]]: # [ [" "], [" "] ]
    sub1 = defaultdict(list) # { "key" : [] } -> by default, any key is an empty list

    for word in strs:
        wordStore = [0] * 26 # [0,0,0,0,0,...] 
        # [1,0,2,0,0,0,0, ...]
        # str([1,0,2,0,0,0,0, ...])
        # sub[str([1,0,2,0,0,0,0, ...])].append(word)
        for char in word:
            #ord(char) -> unicode value of a character
            #ex: ord("c") - ord("a") = 99 - 97 = 2 (3rd index) 
            wordStore[ord(char) - ord("a")] += 1
            
        sub1[str(wordStore)].append(word)
        
    return list(sub1.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))