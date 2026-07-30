class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentProfit = 0
        maxProfit = 0
        last = prices[0]
        for p in prices:
            currentProfit += p - last
            if currentProfit < 0:
                currentProfit = 0
            if maxProfit < currentProfit:
                maxProfit = currentProfit
            last = p
        return maxProfit