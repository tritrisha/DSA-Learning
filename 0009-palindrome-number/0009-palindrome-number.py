class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=0
        n=x
        if x<0:
            return False
        while x:
            r= (x%10)+ (r*10)
            x//=10
        return r==n

        