class Solution:
    def maxProduct(self, n: int) -> int:
        k=[]
        while n:
            k.append(n%10)
            n//=10
        m=k.pop(k.index(max(k)))

        return max(k)*m
        



        