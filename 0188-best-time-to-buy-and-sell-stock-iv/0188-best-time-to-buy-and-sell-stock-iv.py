class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n=len(prices)
        if n==1:
            return 0
        def tryy(day, buy, cap):
            if day>=len(prices):
                return 0

            if dp[day][buy][cap]!=-1:
                return dp[day][buy][cap]

            if buy and cap>0:
                dp[day][buy][cap]=max(-prices[day]+tryy(day+1, 0, cap-1),
                            tryy(day+1, 1, cap) )

            elif not buy:
                dp[day][buy][cap]=max(prices[day]+tryy(day+1, 1, cap),
                            tryy(day+1, 0, cap) )

            else:
                dp[day][buy][cap]=0


            return dp[day][buy][cap]

       
        dp=[[[-1]*(k+1) for _ in range(2)] for _ in range(n)]
        p=tryy(0, 1, k)
        return p
        
        