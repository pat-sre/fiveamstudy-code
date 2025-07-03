def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    count = {}
    for i in nums:
        count[i] = count.get(i, 0) + 1

    idx = 0
    for i in [0, 1, 2]:
        for j in range(count[i]):
            nums[idx] = i
            idx += 1
    print(nums)

nums = [2,0,2,1,1,0]
sortColors(nums)