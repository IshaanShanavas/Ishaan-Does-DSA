class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current = prices[0]


        for i in range (0, len(prices)):
            if prices[i] < current:
                current = prices[i]
            elif prices[i] - current > 0:
                profit += prices[i] - current
                if i <= len(prices):
                    current = prices[i]
        
        return profit
        