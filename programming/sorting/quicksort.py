def quickSort(nums, pivot="last"):
    if len(nums) <= 1:
        return nums
    split(0, len(nums)-1, nums)
    return nums

def split(start, end, nums):
    if start >= end:
        return
    l = partition(start, end, nums)

    split(start, l-1, nums)
    split(l+1, end, nums)


def partition(start, end, nums):
    left = start
    curr = left
    pivot = nums[end]
    while curr < end:
        if nums[curr] <= pivot:
            nums[curr], nums[left] = nums[left], nums[curr]
            left += 1
        curr += 1
    nums[end], nums[left] = nums[left], nums[end]
    
    return left
    




assert quickSort([]) == []
assert quickSort([1]) == [1]
assert quickSort([3,2,1,0])
assert quickSort([3,1,3,2,1,3,1,2]) == [1,1,1,2,2,3,3,3]
#print(order(0, 4, [0,2,5,4,0]))
nums = [3,2,1,4,1,2]
print(quickSort(nums))
#print(parition(0,0,[123]))