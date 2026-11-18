class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0:
            return 0
        p=[1]*n
        p[0]=0
        if n>=2:
            p[1]=0
        for i in range(2, n):
            if p[i]==1:
                for j in range(i*2, n, i):
                    if j==i or p[j]==0:
                        continue
                    if j%i==0:
                        p[j]=0

        return p.count(1)

