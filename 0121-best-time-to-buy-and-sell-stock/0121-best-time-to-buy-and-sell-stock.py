class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        curr_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if (curr_price > prices[i]):
                curr_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - curr_price)
                
        return max_profit