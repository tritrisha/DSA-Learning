class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            k=1
            for i in str(n):
                k=k*int(i)

            if k%t==0:
                return n

            n=n+1

            



        