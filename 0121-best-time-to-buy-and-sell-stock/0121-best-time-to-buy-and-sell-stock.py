class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        current = prices[0]

        for i in prices:
            if i < current:
                current = i
            elif i - current > max_diff:
                max_diff = i - current

        
        return max_diff



        