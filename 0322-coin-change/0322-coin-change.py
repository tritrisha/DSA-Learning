class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        def coin(i, a):
            if a<0 or i>=len(coins):
                return float('inf')
            if a==0:
                return 0
            
            if dp[a][i]!=-1:
                return dp[a][i]

            pick=coin(i, a-coins[i])+1
            notpick=coin(i+1, a)
            dp[a][i]=min(pick , notpick)
            return dp[a][i]

        dp=[[-1]*len(coins) for _ in range(amount+1)]
        ans=coin(0, amount)
        if ans!=float('inf'):
            return ans
        else:
            return -1
        

        