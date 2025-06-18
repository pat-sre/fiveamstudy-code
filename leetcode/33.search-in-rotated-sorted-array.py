#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l

        idx = self.bin_search(0, pivot)
        if idx != -1:
            return idx

        return self.bin_search(pivot, len(nums) - 1)

        

    def bin_search(self, start, end, nums, target):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] <= target:
            return self.bin_search(mid + 1, end, nums, target)
        else:
            return self.bin_search(start, mid - 1, end, nums, target)

        
# @lc code=end

#nums = [4,5,6,7,0,1,2]
nums = [9,1,2,3,4,5,6,7,8]
l = 0
r = len(nums) - 1
while l < r:
    mid = (l + r) // 2
    print(l, mid, r)
    if nums[mid] > nums[r]:
        l = mid + 1
    else:
        r = mid
print(l, r)