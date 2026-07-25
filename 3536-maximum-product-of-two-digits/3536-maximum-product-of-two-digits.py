class Solution:
    def maxProduct(self, n: int) -> int:
        k=[]
        while n:
            k.append(n%10)
            n//=10
        m=0
        for i in range(len(k)):
            for j in range(len(k)):
                if i==j:
                    continue
                else:
                    m=max(m, k[i]*k[j])
        return m




        