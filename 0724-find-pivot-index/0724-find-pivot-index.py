class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        ps1=[0]*n
        ps2=[0]*(n)
        for i in range(len(nums)):
            ps1[i]=ps1[i-1]+nums[i]                  
            ps2[n-i-1]=ps2[-i]+nums[n-i-1] 

        for i in range(len(ps1)):
            if ps1[i]==ps2[i]:
                return i

        return -1
            
        