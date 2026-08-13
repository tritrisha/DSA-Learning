class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=0
        xx=nums[0]
        for i in range(len(nums)):
            m=max(nums[i], m+nums[i])
            if xx<m:
                xx=m

        return xx


        