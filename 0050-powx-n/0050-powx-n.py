class Solution:
    def myPow(self, x: float, n: int) -> float:
        def p(i, j):
            if j==0:
                return 1
            if j==1:
                return i
            if j%2==0:
                return p(i*i, j//2)

            else:
                return i*p(i, j-1)

            
        if n>0:
            return p(x, n)
        else:
            n=n*-1
            return 1/p(x, n)


        

        
        