class Solution:
    def numDecodings(self, s: str) -> int:
        n1=1
        if s[0]!='0':
            n2=1
        else:
            return 0
        
        for i in range(2, len(s)+1):
            temp=0
            oned=int(s[i-1:i])
            twod=int(s[i-2:i])

            if oned>=1:
                temp+=n2

            if twod>=10 and twod<=26:
                temp+=n1

            n1, n2= n2, temp

            
        return n2



        