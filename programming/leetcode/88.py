def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # following leetcoding guide on the right
    
def three_pointers_better(nums1, m, nums2, n) -> None:
    # we use two pointers, traverse from the end
    ptr_a = m-1
    ptr_b = n-1
    ptr = n+m-1
    while ptr_a >= 0 and ptr_b >= 0:
        if nums1[ptr_a] > nums2[ptr_b]:
            nums1[ptr] = nums1[ptr_a]
            ptr_a -= 1
        else:
            nums1[ptr] = nums2[ptr_b]
            ptr_b -= 1 
        ptr -= 1 
    
    while ptr_a >= 0:
        nums1[ptr] = nums1[ptr_a]
        ptr_a -= 1
        ptr -= 1
    
    while ptr_b >= 0:
        nums1[ptr] = nums2[ptr_b]
        ptr_b -= 1
        ptr -= 1

    


def three_pointers(nums1, nums2):
    ptr = 0
    ptr_a = 0
    ptr_b = 0
    nums_1a = [nums1[i] for i in range(len(nums1) - len(nums2))]
    while ptr_a < len(nums_1a) and ptr_b < len(nums2):
        if nums_1a[ptr_a] < nums2[ptr_b]:
            nums1[ptr] = nums_1a[ptr_a]
            ptr_a += 1
        else:
            nums1[ptr] = nums2[ptr_b]
            ptr_b += 1
        ptr += 1
    
    while ptr_a < len(nums_1a):
        nums1[ptr] = nums_1a[ptr_a]
        ptr_a += 1
        ptr += 1
    
    while ptr_b < len(nums2):
        nums1[ptr] = nums2[ptr_b]
        ptr_b += 1
        ptr += 1