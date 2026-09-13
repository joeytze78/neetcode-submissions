class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Input: prices = [10,1,5,6,7,1]
        # Output: 6
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    profit = max(profit, abs(prices[i] - prices[j]))
        
        return profit