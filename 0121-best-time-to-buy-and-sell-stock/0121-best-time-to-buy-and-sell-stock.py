class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prize = float("inf")
        max_profit = 0

        for i in prices:
            if i< min_prize:
                min_prize = i
            
            profit =i-min_prize
            if profit > max_profit:
                max_profit = profit

        return max_profit