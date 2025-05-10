def bubblesort(nums: list) -> list:
    #for i in range(len(nums)):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
    return nums

def recursive_bubble(nums: list, end: int) -> list:
    if end <= 1:
        return nums
    for i in range(end - 1):
        if nums[i] > nums[i+1]:
            nums[i+1], nums[i] = nums[i], nums[i+1]

    recursive_bubble(nums, end - 1)
    return nums

nums = [1,4,2,7,2,3,6,6,8,1,6,9,2]
print(bubblesort(nums))

nums = [1,4,2,7,2,3,6,6,8,1,6,9,2]
print(recursive_bubble(nums, len(nums)))
