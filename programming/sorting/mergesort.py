def mergeSort(nums):
    if len(nums) < 2:
        return nums
    return split(0, len(nums)-1, nums)
    

def split(start, end, nums):
    if start == end:
        return
    
    mid_point = start + (end - start) // 2
    
    split(start, mid_point, nums)
    split(mid_point+1, end, nums)

    mergeSubarrays(start, mid_point, mid_point+1, end, nums)
    return nums


# memory complexity is O(n log n) i think, with this function after all merges
def mergeSubarrays(start1, end1, start2, end2, nums):
    if start2 < start1:
        raise ValueError
    arr1 = nums[start1:end1+1].copy()
    arr2 = nums[start2:end2+1].copy()
    ptr1, ptr2 = 0, 0
    ptr = start1
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] < arr2[ptr2]:
            nums[ptr] = arr1[ptr1]
            ptr += 1
            ptr1 += 1
        else:
            nums[ptr] = arr2[ptr2]
            ptr += 1
            ptr2 += 1
    while ptr1 < len(arr1):
        nums[ptr] = arr1[ptr1]
        ptr += 1
        ptr1 += 1
    while ptr2 < len(arr2):
        nums[ptr] = arr2[ptr2]
        ptr += 1
        ptr2 += 1
    
    return nums

nums = [0,4,3,2,3,1,2,0,5,1]
#print(mergeSubarrays(0, 2, 3, 4, nums))

assert mergeSort([]) == []
assert mergeSort([1]) == [1]
assert mergeSort([3,2,1,0])
assert mergeSort([3,1,3,2,1,3,1,2]) == [1,1,1,2,2,3,3,3]

print(mergeSort(nums))    