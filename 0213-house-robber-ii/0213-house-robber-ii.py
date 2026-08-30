class Solution:
    def rob(self, nums: List[int]) -> int:
        x=len(nums)
        dp=[0]*x
        if x==1:
            return nums[0]
        for i in range(0, x-1):
            dp[i]=max(nums[i]+dp[i-2], dp[i-1])
        pick1=dp[i]

        
        dp=[0]*x
        for i in range(1, x):
            dp[i]=max(nums[i]+dp[i-2], dp[i-1])

        return max(pick1, dp[i])


        