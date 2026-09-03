class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length=len(nums)
        total=sum(nums)
        left=0
        for i in range(length):
            right=total-nums[i]-left
            if right==left:
                return i

            left+=nums[i]

        return -1

            


