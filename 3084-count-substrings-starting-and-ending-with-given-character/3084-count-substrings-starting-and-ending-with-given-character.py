class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        left=0
        right=0
        cou=0
        for i in s:
            if i==c:
                cou+=1

        return (cou*(cou+1))//2

            
            
            

        