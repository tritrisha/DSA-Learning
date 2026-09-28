class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def hr(x, n):
            if x==n-1:
                return nums[n-1]

            if x==n:
                return 0

            if dp[x]!=-1:
                return dp[x]
                
            dp[x]=max(hr(x+1, n), hr(x+2, n)+nums[x])
            return dp[x]


        dp=[-1]*len(nums)
        one=hr(0, len(nums)-1)
        dp=[-1]*len(nums)
        two= hr(1, len(nums))
        return max(one, two)

        