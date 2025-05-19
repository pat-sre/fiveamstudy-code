from typing import List


def trap(height: List[int]) -> int:
# following the LeetCoding guide on bottom right
    if len(height) == 1:
        raise NotImplementedError()
    water = 0
    # from the left till mid
    i = 0
    high = height[i]
    mid_point = len(height) // 2
    while i < mid_point:
        if height[i] > high:
            high = height[i]
        else:
            water += high - height[i]
        i += 1
    # from the right till mid
    high_i = high
    j = len(height) - 1
    high = height[j]
    while j > mid_point:
        if height[j] > high:
            high = height[j]
        else:
            water += high - height[j]
        j -= 1
    # last case, what to do about i=mid_point=j
    water += max(high_i, high) - height[mid_point]
    return water
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))

height = [4,2,0,3,2,5]
print(trap(height))