class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        lowest = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - lowest
            if profit > max_profit:
                max_profit = profit
            elif prices[i] < lowest:
                lowest = prices[i]

        return max_profit