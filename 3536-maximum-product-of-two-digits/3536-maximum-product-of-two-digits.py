class Solution:
    def maxProduct(self, n: int) -> int:
        k=[]
        while n:
            heappush(k, -(n%10))
            n//=10

        m=heappop(k)

        return k[0]*m

        
        



        