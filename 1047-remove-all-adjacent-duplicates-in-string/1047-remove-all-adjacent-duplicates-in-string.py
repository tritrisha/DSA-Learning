class Solution:
    def removeDuplicates(self, s: str) -> str:
        f=-1
        r=[]

        for i in range(0, len(s)):
            if not r:
                r.append(s[i])
                f+=1            
            elif r[f]!=s[i]:
                r.append(s[i])
                f+=1

            elif r[f]==s[i]:
                r.pop()
                f-=1


        return "".join(r)

            

                


        