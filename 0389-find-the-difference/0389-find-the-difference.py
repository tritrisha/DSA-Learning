class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r=t
        for i in s:
            if i in t:
                print(i)
                r=r.replace(i, "", 1)

        return r


        
            

        
        