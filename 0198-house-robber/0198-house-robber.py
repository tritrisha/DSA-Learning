class Solution:
    def rob(self, nums: list[int]) -> int:
        def hr(x):
            if x==0:
                return nums[0]
            if x==-1:
                return 0

            if dp[x]!=-1:
                return dp[x]
            dp[x]=max(hr(x-1), hr(x-2)+nums[x])
            return dp[x]
                
                
        dp=[-1]*len(nums)
        return hr(len(nums)-1)

        
        

        
        