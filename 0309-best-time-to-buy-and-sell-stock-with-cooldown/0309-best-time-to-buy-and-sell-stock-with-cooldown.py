class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        def tr(buy, ind):
            if ind>=p:
                return 0


            if dp[buy][ind]!=-1:
                return dp[buy][ind]
            
            if buy:
                dp[buy][ind]=max(-prices[ind]+tr(0, ind+1), tr(1, ind+1))
            else:
                dp[buy][ind]=max(prices[ind] + tr(1, ind+2), tr(0, ind+1))

            return dp[buy][ind]



        
        p=len(prices)
        dp=[[-1]*p for _ in range(2)]
        return tr(1, 0)