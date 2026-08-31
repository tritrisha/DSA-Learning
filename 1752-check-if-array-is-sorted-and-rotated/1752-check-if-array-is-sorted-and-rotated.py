class Solution:
    def check(self, nums: List[int]) -> bool:
        x=0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                x+=1

        if nums[0]<nums[-1]:
            x+=1
        return x<=1

            


        

        