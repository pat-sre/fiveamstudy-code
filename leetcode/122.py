from typing import List

def maxProfit(prices: List[int]) -> int:
    # following the leetcoding guide
    if len(prices) == 1:
        return 0
    l = 0
    r = 1
    max_profit = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            max_profit = max(max_profit, prices[r] - prices[l])
        else:
            l = r
        r += 1
    return max(max_profit, 0)