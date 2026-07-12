class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            x=math.log2(n)
            if x==0 or x==int(x):
                return True
            else:
                return False

        else:
            return False

        
        