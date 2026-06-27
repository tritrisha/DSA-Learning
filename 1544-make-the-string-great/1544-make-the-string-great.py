class Solution:
    def makeGood(self, s: str) -> str:
        r=[s[0]]
        k=0
        for i in range(1, len(s)):
            if not r:
                r.append(s[i])
                k+=1
            elif s[i].isupper() and r[k]==s[i]:
                r.append(s[i])
                k+=1
            elif s[i].isupper() and r[k].upper()==s[i]:
                r.pop()
                k-=1

            elif s[i].islower() and r[k]==s[i].upper():
                r.pop()
                k-=1

            

            else:
                r.append(s[i])
                k+=1

            
        


        return ''.join(r)
        