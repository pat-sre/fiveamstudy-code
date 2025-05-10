def recursive_sum(numbers: list) -> int:
    if numbers == []:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])


nums = [1, 2, 3, 10]
print(recursive_sum(nums))