class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxcount=0 
        f=0
        l=0
        z=nums.count(0)
        if k>z:
            k=z

        for i in nums:
            if i==0:
                k-=1
            if k==0:
                maxcount=max(maxcount, l-f+1)
            if k<=-1:
                f+=1
                if nums[f-1]==0:
                    k+=1

            l+=1

        return maxcount

            

            




            


        