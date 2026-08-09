def bin_search(nums, target):
    left, right = 0, len(nums) - 1
    
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    
    return -1



    

if __name__ == "__main__":
    nums = [1,3,4,5,7,9,12,14,17,20]
    print(bin_search(nums, 6))

