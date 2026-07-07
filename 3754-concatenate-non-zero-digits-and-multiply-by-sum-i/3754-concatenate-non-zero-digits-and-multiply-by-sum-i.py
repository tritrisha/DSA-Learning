class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num=n
        sums=0
        r=0
        mul=1
        while num:
            x=num%10
            num//=10
            if x!=0:
                sums+=x
                r=r+x*mul
                mul*=10
            

        return r*sums


        