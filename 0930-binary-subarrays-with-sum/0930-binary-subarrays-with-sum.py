class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        c=0
        s=0
        n=len(nums)
        h={0:1}
        for i in range(n):
            s+=nums[i]
            if s-goal in h:
                c+=h[s-goal]

            h[s]=h.get(s, 0)+1

        return c

        