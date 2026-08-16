from collections import defaultdict

#Longest Subarray With No Repeated Values
#Given an integer array nums, return length of longest contiguous 
#subarray containing no duplicate values

#Use sliding window technique
#Target O(n) time

# hashmap
# value -> index
# 1 -> index 0
# 2 -> index 1
# 3 -> index 2

#ex1: nums = [1,2,3,2,1] output = 3
#ex2: nums = [4,2,4,5,6] output = 4
#ex3: nums = [1,2,3,2,4,5] output = 4
#ex:4 nums = [7,7,7,7] output = 1

#nums = [1,2,2,1]
#            L
#              R   

#if the value is in the hashmap, set the starting pointer to the value's index + 1

#hashmap
# 1 -> 0
# 2 -> 2

# [1,2,2,1]
#      L
#        R

#hashmmap
# 1 -> 3
# 2 -> 2

#unique_array = 2

def longestNoRepeatedValues(nums):
    unique_nums = defaultdict(int)
    left = 0
    unique_array = 0
    
    for right in range(len(nums)):
        if nums[right] in unique_nums and unique_nums[nums[right]] >= left:
            left = unique_nums[nums[right]] + 1
        
        unique_nums[nums[right]] = right
          
        unique_array = max(unique_array, right - left + 1)
        
    return unique_array

#O(n) time complexity where n is the length of nums
#O(m) space complexity where m is the number of unique nums


if __name__ == "__main__":
    nums = [1,2,3,1,2]
    print(longestNoRepeatedValues(nums))