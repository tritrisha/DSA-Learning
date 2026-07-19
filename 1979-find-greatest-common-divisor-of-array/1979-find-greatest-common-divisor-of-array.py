class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini=min(nums)
        r=mini
        maxi=max(nums)
        while r>0 and (maxi%r!=0 or mini%r!=0) :
            r-=1

        return r


        