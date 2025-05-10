def quicksort(numbers: list, start: int, end: int) -> list:
    if end <= start: 
        return [numbers[start]]
    numbers = partition(numbers, start, end)
    print(f"{numbers=}")
    
    mid_point = (start + end) // 2

    print(f"left_half, {start=}, end={mid_point}")
    left_half = quicksort(numbers, start, mid_point)
    print(f"left_half, start={mid_point + 1}, end={end}")
    right_half = quicksort(numbers, mid_point + 1, end - 1)

    print(f"{left_half=} + {right_half=}")
    return left_half + right_half
    

def partition(arr: list, start: int, end: int) -> list:
    pivot = arr[start]
    i: int = start + 1
    j: int = end
    while i < j:
        if arr[i] <= pivot:
            i += 1
        if arr[j] > pivot:
            j -= 1
        #if arr[j] > arr[i]:
        arr[j], arr[i] = arr[i], arr[j]
    #print("before last swap:", arr)
    if arr[j] < arr[start]:
        arr[j], arr[start] = arr[start], arr[j]
    #print("after last swap:", arr)
    return arr
numbers = [1, 8, 1, 2, 4, 6, 5, 7, 9]
print(quicksort(numbers, 0, len(numbers)-1))

#numbers = [7, 8, 9, 1, 2, 10]
#print(partition(numbers, 2, len(numbers) - 1))
#print(quicksort(numbers, 0, len(numbers)-1))