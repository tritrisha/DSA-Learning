class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        h={0:1}
        s=0
        c=0
        for i in range(n):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
            s+=nums[i]
            if s-k in h:
                c+=h[s-k]
            h[s]=h.get(s, 0)+1
        return c
            







        