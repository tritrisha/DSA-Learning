class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        s=0
        for i in range(n):
            nosa=(i+1) * (n-i)
            osa=(nosa+1)//2
            s+=(osa*arr[i])

        return s

            



        