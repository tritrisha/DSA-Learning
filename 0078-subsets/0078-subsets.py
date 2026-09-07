class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subs(x, s):
            k.append(s)
            for i in range(x, len(nums)):
                subs(i+1, s+[nums[i]])

        k=[]
        subs(0, [])
        return k
        