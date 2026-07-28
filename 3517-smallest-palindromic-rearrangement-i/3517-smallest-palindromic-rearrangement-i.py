class Solution:
    def smallestPalindrome(self, s: str) -> str:
        x=len(s)//2
        if x==0:
            return s
        hs=sorted(s[:x])
        h="".join(hs)
        if len(s)%2==0:
            return h+h[::-1]

        else:
            return h+s[x]+h[::-1]

        

        