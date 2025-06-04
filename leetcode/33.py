from typing import List
def search(nums: List[int], target: int) -> int:
    # following the 5 am leetcoding guide
    # unrotating is breaking O(log n) constraint as it's O(n)
    # i think we need to run bin search to find the rotation point
    # what if i run bin search to find if the SORTED ARRAY property holds?
    pass

def bin_search(left, right, nums, target):
    print(left, right)
    if left > right:
        return None

    mid_point = left + (right - left) // 2
    if nums[mid_point] == target:
        return mid_point
    elif target > nums[mid_point]:
        return bin_search(mid_point+1, right, nums, target)
    else:
        return bin_search(left, mid_point-1, nums, target)

def find_breakpoint(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        #print(l, r)
        if r - l == 1:
            return r
        mid_point = l + (r - l) // 2
        if nums[l] > nums[mid_point]: # we know theres breakpoint in the left side as nums[l] < mid_point
            r = mid_point
        elif nums[r] < nums[mid_point]:
            l = mid_point
        else:
            break
            


nums = [4,5,6,7,0,1,2]
target = 0
r = find_breakpoint(nums)
for i in range(len(nums)):
    idx = (i + r) % len(nums)
    print(nums[idx], end = " ")

print()
#print(bin_search(0, len(nums) - 1, nums, target))
#print(find_breakpoint(nums))

nums = [1,2,3,4,0]
r = find_breakpoint(nums)

for i in range(len(nums)):
    idx = (i + r) % len(nums)
    print(nums[idx], end = " ")

print()

