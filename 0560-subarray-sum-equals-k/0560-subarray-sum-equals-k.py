class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        presum=[0]*(len(nums))
        for i in range(len(nums)):
            presum[i]=presum[i-1]+nums[i]

        print(presum)
        h={0:1}
        for i in presum:
            p=i-k
            if p in h:
                c+=h[p]
            if i in h:
                h[i]+=1
            else:
                h[i]=1  
        return c

            




        