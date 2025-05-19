from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
        # indices dont really matter, its about numbers
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        missing_pieces = {}
        # i can filter incorrect triplets 
        while left < right:
        # as left is the smallest number, we wont find a smaller number 
        # as right is the biggest number, we wont find a bigger number
            missing_piece = nums[right] + nums[left]
            if nums[left] > missing_piece > nums[right]:
                missing_pieces[missing_piece].append([nums[right], nums[left]])
                left += 1
            elif missing_piece > nums[right]:
                right -= 1
            elif missing_piece < nums[left]:
                left += 1
        print(missing_pieces)

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))