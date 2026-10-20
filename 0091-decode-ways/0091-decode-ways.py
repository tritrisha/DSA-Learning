class Solution:
    def numDecodings(self, s: str) -> int:
        def numbers(x, c):
            if x>=len(s):
                return 1
            if s[x]=='0':
                return 0
            if dp[x]!=-1:
                return dp[x]
            
            c=numbers(x+1, c)
            if x+1<len(s) and int(s[x:x+2])<=26:
                c+=numbers(x+2, c)

            dp[x]=c
            return dp[x]


        dp=[-1]*len(s)
        return numbers(0, 0)



        