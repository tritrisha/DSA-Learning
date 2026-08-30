class Solution:
    def rob(self, nums: List[int]) -> int:
        x=len(nums)
        def money(n):
            if n>=x:
                 return 0
            if dp[n]!=-1:
                return dp[n]
            
            pickn=nums[n]+money(n+2)
            notpick=money(n+1)
            dp[n]=max(pickn, notpick)
            return dp[n]

        
        dp=[-1]*x
        return money(0)

        