from typing import List

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
        # following the leetcoding guide
        return bruteforce(nums1, nums2)

def stack_solution(nums1, nums2):
     # following the 5 AM leetcoding guide :)
    nums2_lookup = {i: idx for idx, i in enumerate(nums2)}
    stack = []
    greater = [-1 for _ in nums2]

    for i in range(len(nums2)):
        idx = len(nums2) - 1 - i
        curr_num = nums2[idx]
        while len(stack) > 0 and curr_num > stack[-1]:
            stack.pop()
        if len(stack) > 0:
            greater[idx] = stack[-1]
        stack.append(curr_num)
    sol = [greater[nums2_lookup[num1]] for num1 in nums1]
    return sol

def bruteforce(nums1, nums2):
    solution = []
    for num in nums1:
        is_found = False
        next_largest = -1
        for num2 in nums2:
            if num == num2:
                is_found = True
            elif not is_found:
                continue
            elif is_found and num2 > num:
                next_largest = num2
                break
        solution.append(next_largest)
    return solution