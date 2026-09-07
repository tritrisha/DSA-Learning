class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def check(p):
            if p==0:
                return False

            if p==1:
                return True

            if p%2==0:
                return check(p//2) 

            else:
                return False


        return check(n)
        