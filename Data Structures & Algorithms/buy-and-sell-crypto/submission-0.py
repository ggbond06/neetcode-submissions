class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, price1 in enumerate(prices):
            for j, price2 in enumerate(prices[i + 1:], start = i + 1):
                temp = price2 - price1
                if temp > max_profit:
                    max_profit = temp
        
        return max_profit
        