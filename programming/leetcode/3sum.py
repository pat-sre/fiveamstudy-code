from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    # indices dont really matter, its about numbers
    triplets = []
    nums = sorted(nums)
    fixd = 0
    prev = None
    while fixd < len(nums) - 2:  
        # fix the number, use it as target for 2sum
        # a + b + c = 0 -> a + b = -c

        target = -1 * nums[fixd]
        if nums[fixd] != prev:
            triplets.extend(twoSum(nums, fixd + 1, target))
        prev = nums[fixd]
        fixd += 1
        
    return triplets

                
def twoSum(nums, start, target):
    # here we want to find 2 numbers that sum up to a fixed number 
    l = start
    r = len(nums) - 1
    two_sums = []
    prev_l = None
    prev_r = None
    # we need duplicate skipping mechanism in place
    while l < r: # array is sorted, we can two pointer it
        two_sum = nums[l] + nums[r]
        if two_sum == target:
            if nums[l] != prev_l and nums[r] != prev_r:
                two_sums.append([-target, nums[l], nums[r]])
            prev_l = nums[l]
            l += 1
        elif two_sum > target:
            prev_r = nums[r]
            r -= 1
        elif two_sum < target:
            prev_l = nums[l]
            l += 1

    print(f"{target=}, {two_sums=}")
    return two_sums

nums = [0,0,0,0]
print(threeSum(nums))