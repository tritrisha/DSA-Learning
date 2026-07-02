class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        r=[]
        m=max(nums)
        for i in range(len(nums)):
            if nums[i]!=m:
                r.append(nums[i]*2)

            else:
                c=i


        for i in r:
            print(i)
            if i>m:
                return -1

        return c
