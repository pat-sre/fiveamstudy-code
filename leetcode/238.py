from typing import List

def productExceptSelf_2arrays(nums: List[int]) -> List[int]:
    # 1. create prefix and suffix product arrays
    prefix = [nums[0]]
    suffix = [nums[len(nums) - 1]]
    for i in range(1, len(nums), 1):

        prefix.append(prefix[i - 1] * nums[i])
        suffix.append(suffix[i - 1] * nums[len(nums) - i - 1])
    suffix.reverse()
    
    print(f"{prefix=}")
    print(f"{suffix=}")
    print(f"{nums=}")
    # solution is prefix[i-1] * suffix[i+1]
    solution = [suffix[1]]
    for i in range(1, len(nums) - 1, 1):
        solution.append(prefix[i - 1] * suffix[i + 1])
    # last is just last prefix nvm its good nvm its wrong xD
    solution.append(prefix[-2])
    print(f"{solution=}")
    print("-----")
    return solution


def productExceptSelf(nums: List[int]) -> List[int]:
    # lets try implementing the better solution 
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(ans[i-1] * nums[i])
        suffix = nums[-1]
        for i in range(1, len(nums)):
            ans[i] = X * suffix
            suffix *= nums[-i]
        print(f"{nums=}")
        print(f"{ans=}")
        #for i in range(len(nums)):
        return []


nums = [1,2,3,4]
print(productExceptSelf(nums))


nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))

nums = [2,1]
print(productExceptSelf(nums))

nums = [-3, 1, 3]
print(productExceptSelf(nums))
