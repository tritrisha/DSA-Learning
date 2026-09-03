class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        maxaltitude=0
        prev=0
        for i in range(1, n+1):
            prev=gain[i-1]+prev
            maxaltitude=max(maxaltitude, prev)
            

        return maxaltitude


        