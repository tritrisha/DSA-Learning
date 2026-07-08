class Solution:
    def firstUniqChar(self, s: str) -> int:
        m={}
        for i in s:
            if i not in m:
                m[i]=1

            else:
                m[i]+=1

        for i in m:
            if m[i]==1:
                return s.index(i)

        return -1

        