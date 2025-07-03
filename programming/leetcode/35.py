def searchInsert(nums, target: int) -> int:
    # following the 5 am leetcoding guide 

    #return bin_search(0, len(nums), target, nums)

def bin_search(left, right, target, nums):
    if left > right:
        return -1
    mid_point = left + (right - left) // 2
    if right - left == 1 and nums[mid_point] != target:
        return -1

    if target > nums[mid_point]: 
        return bin_search(mid_point, right, target, nums)
    elif target < nums[mid_point]: 
        return bin_search(0, mid_point, target, nums)
    else:
        return mid_point
    
nums = [2, 5]
target = 5
print(searchInsert(nums, target))