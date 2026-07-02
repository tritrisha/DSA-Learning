class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m=max(nums)
        nums.remove(m)
        return (m-1)*(max(nums)-1)

        