class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        l=len(nums)
        i=0
        res=0
        md=0
        for k in nums:
            res=max(res, md*k)     
            md=max(md, i-k)
            i=max(i, k)     

        return res 


        
        

            



        