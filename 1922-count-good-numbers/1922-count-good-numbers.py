class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=1000000007
        def poww(x, r, mod):
            x=x%mod
            if r==1:
                return x%mod
            if r==0:
                return 1

            if r%2==0:
                return poww((x*x), r//2, mod)

            else:
                return x*poww(x, r-1, mod)

        if n==1:
            return 5

        if n%2==0:
            r=n//2
            return (poww(5, r, mod)*poww(4, r, mod))%mod

        if n%2!=0:
            r=n//2
            return (poww(5, r+1, mod)*poww(4, r, mod))%mod
        

        

            

        