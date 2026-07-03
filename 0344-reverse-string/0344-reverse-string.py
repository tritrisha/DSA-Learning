class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        k=[]
        for i in s:
            k.append(i)
        p=len(s)-1
        for i in range(len(k)):
            s[p]=k[i]
            p-=1

        
        