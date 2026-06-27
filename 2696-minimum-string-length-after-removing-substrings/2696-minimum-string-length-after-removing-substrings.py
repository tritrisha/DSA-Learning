class Solution:
    def minLength(self, s: str) -> int:
        r=[s[0]]
        f=0
        for i in range(1, len(s)):
            if not r:
                r.append(s[i])
                f+=1

            elif r[f]=='A' and s[i]=='B':
                r.pop()
                f-=1

            elif r[f]=='C' and s[i]=='D':
                r.pop()
                f-=1


            else:
                r.append(s[i])
                f+=1

        return len(r)


        