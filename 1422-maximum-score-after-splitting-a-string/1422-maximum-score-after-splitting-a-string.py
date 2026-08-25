class Solution:
    def maxScore(self, s: str) -> int:
        m=0
        n=len(s)
        for i in range(1, len(s)):
            p=s[:i].count('0')+s[i:].count('1')
            m=max(p, m)

        return m


            




        
        