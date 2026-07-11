class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        s=0
        for l in range(n):
            r=l+1
            while abs(r-l)%2!=0:
                s+=sum(arr[l:r])
                r+=1
                if (r-l)%2==0 and r<n:
                    r+=1

        return s

            



        