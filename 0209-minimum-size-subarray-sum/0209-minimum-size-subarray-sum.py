class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m=10**9
        n=len(nums)
        s=0
        j=0
        for i in range(n):
            s+=nums[i]
            while s>=target:
                m=min(m, i-j+1)
                s-=nums[j]
                j+=1

        
        if m==10**9:
            return 0
        else:
            return m
            

        