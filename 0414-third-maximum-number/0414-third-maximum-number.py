class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        r=[]
        for i in nums:
            if i not in r:
                r.append(i)
        
        if len(r)<3:
            return max(r)
        r.remove(max(r))
        r.remove(max(r))
        return max(r)


        
                

            

        