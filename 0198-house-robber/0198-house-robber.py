class Solution:
    def rob(self, nums: List[int]) -> int:
        x=len(nums)
        if x==1:
            return nums[0]
        inn=nums[0]
        exx=max(nums[0], nums[1])
        for i in range(2, x):
            curr=max(nums[i]+inn, exx)
            inn=exx
            exx=curr

        return exx

        

        