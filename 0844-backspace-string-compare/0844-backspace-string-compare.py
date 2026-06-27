class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        r=[]
        for i in s:
            if i=='#':
                if r:
                    r.pop()
                continue

            else:
                r.append(i)


        x="".join(r)
        r=[]
        for i in t:
            if i=='#':
                if r:
                    r.pop()
                continue

            else:
                r.append(i)


        return x=="".join(r)
        