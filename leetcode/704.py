def search(nums, target: int) -> int:
    #return bin_search(0, len(nums), target, nums)
    left = 0
    right = len(nums) - 1

    while left <= right:
        # define how to narrow the search space
        mid_point = left + (right - left) // 2
        print(mid_point, nums[mid_point])
        if nums[mid_point] > target:
            right = mid_point - 1
        elif nums[mid_point] < target:
            left = mid_point + 1
        else:
            return mid_point
        # choose an exist condition
    return -1


def bin_search(left, right, target, nums):
    if left > right:
        return -1
    mid_point = left + (right - left) // 2
    if right - left == 1 and nums[mid_point] != target:
        return -1
    if target > nums[mid_point]: 
        return bin_search(mid_point, right, target, nums)
    elif target < nums[mid_point]: 
        return bin_search(left, mid_point, target, nums)
    else:
        return mid_point
    
nums = [-1,0,3,5,9,12]
target = 9
print(search(nums, target))

nums = [10]
target = 10
print(search(nums, target))


nums = [2, 5]
target = 5
print(search(nums, target))