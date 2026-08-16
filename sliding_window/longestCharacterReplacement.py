from collections import defaultdict

# 424. Longest Repeating Character Replacement

# You are given a string s and an integer k. 
# You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

# Example 3
# Input: s = "AABBABB", k = 1
#               L
#                   R

# charFreq = { "A" : 1, "B" : 4 }
# substring length = right - left + 1  = 5

# is the current window valid:
# substring length (5) - most common character count (4) = 1 
# if this number calculated is less than or equal to k, the window is valid. if not, the window is invalid

#res = 5

# charFreq = {}
# right = 0
# s = "AAACAB" k = 2
# charFreq["A"] == charFreq[s[right]]

def characterReplacement(s, k):
    charFreq = defaultdict(int) 
    left = 0
    result = 0

    for right in range(len(s)):
        charFreq[s[right]] += 1 #{"A": 1}

        while (right - left + 1) - max(charFreq.values()) > k:
            charFreq[s[left]] -=1 
            left += 1

        result = max(right - left + 1, result)
    
    return result

# time complexity: O(n), n = number of characters in the string 's'.
# space complexity: O(m), m = number of different characters in the string 's'.

#s = "AAABBA"
#charFreq = { "A" : 1, "B" : 1 } 


if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    print(characterReplacement(s,k))

