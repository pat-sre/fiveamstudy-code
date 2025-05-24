def countGoodTriplets(arr, a: int, b: int, c: int):
        # following the 5am leetcoding guide yet again
        # jeez i cant read, i forgot about absolute value T_T, remember read carefully
        return maybeoptimal(arr, a, b, c)

def brute(arr, a, b, c):
    # bruteforce sucks, lets improve it.
    # O(n^3) - computational
    # O(1) - storage
    triplets = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    triplets += 1
    return triplets

def maybeoptimal(arr, a,b,c):
    # sketch
    # hmm what if i substract a from all the numbers, then subtract b from all the numbers and store both outcomes?
    minus_a = {i:x-a for i,x in enumerate(arr)}
    minus_b = {i:x-b for i,x in enumerate(arr)}
    print(f"{arr=}")
    print(minus_a)
    print(minus_b)

arr=[3, 0, 1, 1, 9, 7]
countGoodTriplets(arr, 7, 2, 3)