class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        nums=set(nums)
        if k>len(nums):
            k=len(nums)

        x=[]
        for i in range(k):
            x.append(max(nums))
            nums.remove(max(nums))

        return x

