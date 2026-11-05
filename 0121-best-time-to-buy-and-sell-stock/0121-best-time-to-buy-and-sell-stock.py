class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        for day, pr in enumerate(prices):
            if day==0:
                profit, mini=0, pr
                continue

            cost=pr-mini
            profit=max(profit, cost)
            mini=min(mini, pr)



        return profit

        