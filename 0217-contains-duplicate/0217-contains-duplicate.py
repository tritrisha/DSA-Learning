class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        c=nums[0]
        if len(nums)==1:
            return False
        for i in nums[1:]:
            if c^i==0: 
                return True
            c=i
        return False

        

        