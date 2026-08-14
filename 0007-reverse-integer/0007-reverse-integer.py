class Solution:
    def reverse(self, x: int) -> int:
        
        sign=1
        if x<0:
            sign=-1
            x=-x

        num=0
        while x:
            num=num*10+(x%10)
            x//=10

        r=sign*num
        if r<= -2**31 or r>= 2**31-1:
            return 0

        
        return r



        

        
        
        