class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=1000000007
        if n==1:
            return 5

        if n%2==0:
            r=n//2
            return (pow(5, r, mod)*pow(4, r, mod))%mod

        if n%2!=0:
            r=n//2
            return (pow(5, r+1, mod)*pow(4, r, mod))%mod
        

        

            

        