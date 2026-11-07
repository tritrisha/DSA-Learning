class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        def tryy(buy, sell, profit):
            if buy>=len(prices) or sell>=len(prices):
                return profit

            
            if prices[buy]>prices[sell]:
                return tryy(buy+1, sell+1, profit)

            else:
                return tryy(buy+1, sell+1, profit+prices[sell]-prices[buy])


        return tryy(0, 1, 0)


        
        