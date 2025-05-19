def rotate(nums, k: int):
    nums = nums[k:] + nums[:k]
    return nums

nums = [1,2,3,4,5,6,7]
print(rotate(nums, 2))
