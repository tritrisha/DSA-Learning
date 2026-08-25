class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        m=0
        c=1
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i-1]==nums[i]-1:
                c+=1

            elif nums[i-1]==nums[i]:
                continue

            else:
                if m<c:
                    m=c
                c=1

        if m<c:
            m=c
        return m

                


        




        