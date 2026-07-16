class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n=0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1]==nums[i]:
                nums[i]+=1
                n+=1

            if nums[i-1]>nums[i]:
                x=nums[i-1]-nums[i] + 1
                nums[i]+=x
                n+=x
        
        return n
        
