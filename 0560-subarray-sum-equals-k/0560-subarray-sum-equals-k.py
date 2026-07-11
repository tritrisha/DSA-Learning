class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ps=[0]*n
        for i in range(n):
            ps[i]=ps[i-1]+nums[i]

        hs={0:1}
        count=0
        for i in ps:
            if (i-k) in hs:
                count+=hs[i-k]
                hs[i-k]+=1
            if i in hs and i!=i-k:
                hs[i]+=1
            elif i not in hs:
                hs[i]=1

        return count
            
        


    
        