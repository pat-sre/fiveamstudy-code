def recursive_max(nums: list) -> int:
    if len(nums) == 0:
        return  -99999999
    return max(nums[0], recursive_max(nums[1:]))

numbers = [1, 2, 3, 10, 5, 15]
print(recursive_max(numbers))