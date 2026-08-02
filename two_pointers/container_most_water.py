from typing import List

# 11 Container with most rain water (medium)

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [2,2,2]
# Output: 4

def maxArea(height):
    left = 0
    right = len(height) - 1
    maxContainerArea = 0
    
    while left != right:
        #area = (right index - left index) * min(height[left], height[right])
        area = (right - left) *  min(height[left], height[right])  
        #if new area > maxContainerArea, set maxContainerArea = area 
        maxContainerArea = max(area, maxContainerArea)
        
        if height[right] < height[left]:    
            # decrementing in python
            # if right = 6 then right -= 1 would be 5
            right -= 1
        else:
            left += 1
            
    return maxContainerArea


print(maxArea([1,8,6,2,5,4,8,3,7]))

# time complexity = O(n)
# space complexity = n(1) 