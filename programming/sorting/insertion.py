# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return []
        r = 1
        steps = [pairs.copy()]
        while r < len(pairs):
            l = r - 1
            if pairs[l].key > pairs[r].key:
                pairs[l], pairs[r] = pairs[r], pairs[l]
                # ensure all behind are sorted too
                while l > 0 and pairs[l-1].key > pairs[l].key:
                    pairs[l], pairs[l-1] =  pairs[l - 1], pairs[l]
                    l -= 1
            steps.append(pairs.copy())
            r += 1
        return steps


