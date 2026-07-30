class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentProfit = 0
        maxProfit = 0
        last = prices[0]
        for p in prices:
            currentProfit += p - last
            currentProfit = max(currentProfit, 0)
            maxProfit = max(maxProfit, currentProfit)
            last = p
        return maxProfit