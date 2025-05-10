def mergesort_main(nums: list):
    mergesort(nums, 0, len(nums))

def mergesort(nums: list, start: int, end: int) -> list:
    if start > end:
        return []
    if start == end:
        return nums[start]
    
    split_point = (start + end) // 2
    half1 = mergesort(nums, 0, split_point) # if len(nums) == 10, 0,4
    print(f"{half1=}")
    half2 = mergesort(nums, split_point + 1, len(nums)) # if len(nums) == 10, 5,9
    print(f"{half2=}")
    # we need to merge halves from the recursion stack here
    print(merge(half1, half2))
    return merge(half1, half2)


# use two pointers over halves to merge 
# btw start1,end1,start2,end2 probably more efficient over half1,half2
# TODO: measure differences
def merge(half1: list, half2: list) -> list:
    i, j = 0, 0
    merged = []
    while i < len(half1) and j < len(half2):
        if half1[i] < half2[j]:
            merged.append(half1[i])
            i += 1
        else:
            merged.append(half2[j])
            j += 1
    # append the remaining half1 or half2 that wasnt added during the loop cause one half was shorter
    if i < len(half1):
        merged.append(*half1[i:])
    elif j < len(half2):
        merged.append(*half2[j:])

    return merged



assert(merge([1,3], [2])) == [1,2,3]
assert(merge([], [])) == []
assert(merge([2,4], [1,6])) == [1,2,4,6]

my_list = [1,4,0,15,2]

print(mergesort_main(my_list))