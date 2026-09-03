class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        h={0:-1}
        n=len(nums)
        s=0
        for i in range(n):
            s+=nums[i]
            div=s%k
            if div in h:
                if i-h[div]>1:
                    return True

            h[div]=h.get(div, i)

        return False
