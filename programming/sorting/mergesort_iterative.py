def mergeSort(nums):
    if len(nums) < 2:
        return nums
    
    



assert mergeSort([]) == []
assert mergeSort([1]) == [1]
assert mergeSort([3,1,3,2,1,3,1,2]) == [1,1,1,2,2,3,3,3]
assert mergeSort([3,2,1,0]) == [0,1,2,3]