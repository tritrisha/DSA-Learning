class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit, mini=0, prices[0]
        for pr in prices:
            cost=pr-mini
            profit=max(profit, cost)
            mini=min(mini, pr)
            
        return profit

        