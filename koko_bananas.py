import math

# Koko loves to eat bananas. 
# There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# piles = [25,10,23,4]
# hours = 4
# eatingSpeed = 25

# [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# eatingSpeed = 13
# hours needed at 13 (6) is larger than the hours allowed (4)

# piles = [1,4,3,2]
# hours = 9
# eatingSpeed = 4 -> 4, 3 -> 5, 2 -> 6, 1 -> 10

# left = 1
# right = max(piles)
# [1,2,3,4]

# 3 (pile) / 2 (eating speed) = 1.5 = 2  

# mid (eatingSpeed) = 2
# piles = [1,4,3,2]
# hours = 9
# hoursNeededAtSpeed = ceil(1 / 2) +  ceil(4 / 2) + ceil(3 / 2)  + ceil(1 / 2) = 6
# test the smaller eating speeds

#2 worked, 1 didint work, so 2 is the minimum speed

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


#eatingspeeds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
#piles = [25,10,23,4]
def koko_bananas(piles, h):
    left = 1
    right = max(piles)
    minEatingSpeed = right
 
    while left <= right:
        currEatingSpeed = (left + right) // 2
        hoursNeeded = 0
        for pile in piles:
            hoursNeeded += math.ceil(pile / currEatingSpeed)
        if hoursNeeded <= h:
            minEatingSpeed = currEatingSpeed
            right = currEatingSpeed - 1
        else:
            left = currEatingSpeed + 1
    
    return minEatingSpeed

# time complexity: O(m * logn) 
# m = length of piles 
# n = range of eating speeds to test
# space complexity: O(1)


if __name__ == "__main__":
    # piles = [3,6,7,11]
    # h = 8
    # piles = [30,11,23,4,20]
    # h = 5
    # piles = [30,11,23,4,20]
    # h = 6
    piles = [1,4,3,2]
    h = 9
    # piles = [25,10,23,4]
    # h = 4
    print(koko_bananas(piles, h))