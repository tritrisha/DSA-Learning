class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        def part(i, x):
            if i>=len(nums) or x>target:
                return False
            if x==target:
                return True

            if dp[i][x]!=-1:
                return dp[i][x]

            dp[i][x]=part(i+1, x+nums[i]) or part(i+1, x)
            return dp[i][x]


        if sum(nums)%2!=0:
            return False
        
        target=sum(nums)//2
        dp=[[-1]*target for _ in range(len(nums))]
        return part(0, 0)
        
        
        