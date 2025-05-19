def bruteforce(nums):
        pass

def is_sorted(nums, shift=0):
    # i gotta think how to rotate the array properly
    nums = nums[shift:] + nums[:shift]
    print(nums)
    print(*zip(nums, nums[1:]))  # for visualization purposes
    for i, j in zip(nums, nums[1:]):  # zip just creates a list of tuples to iterate over
        if i > j:
            return False
    return True

def check(nums) -> bool:
    if len(nums) == 1:
        return True
    # ig bruteforce is to check all combinations, thats O(n^2) so kinda bad but fuck it lets do it anyway for now
    #return self.bruteforce(nums)
    # ok now lets improve it 
    # i think this can be done in O(2*n) using sliding window
    nums2 = nums + nums
    window_size = len(nums)
    # the problem becomes, is there a sorted substring of len(nums) in nums2
    # we make at most len(nums) checks
    # if the next number is smaller, instead of bigger, reset the check and start again from it
    valid_substring_len = 0
    i = 0
    while i <= len(nums):
        #print(f"{i=}, {nums2[i]=}, {nums2[i + 1]=}")
        # next number is smaller, we jump the check, to find an increasing number
        if nums2[i] > nums2[i + 1]:
            i += 1
            continue

        valid_substring_len = 0
        
        for j in range(window_size):
            #print(f"{nums2[i+j]} > {nums2[i + j + 1]}")
            if nums2[i + j] > nums2[i + j + 1]:
                #print(f"skipping from to {i} to {i + j + 1}")
                i = i + j + 1
                break
            valid_substring_len += 1
            #print(f"{valid_substring_len=}")
            if valid_substring_len == window_size - 1:
                return True
        #i += 1
    return False

#nums = [1,2,3,4,5]
#for i in range(len(nums)):
#    print(is_sorted(nums, shift=i))
#print(is_sorted(nums))                

nums = [3,4,5,1,2]
print(check(nums))
nums = [2,1,3,4]
print(check(nums)) 