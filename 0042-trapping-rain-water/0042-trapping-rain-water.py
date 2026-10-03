class Solution:
    def trap(self, height: list[int]) -> int:
        n=len(height)        
        pre=[height[0]]*n
        suf=[height[-1]]*n
        for i in range(1, n):
            pre[i]=max(pre[i-1], height[i])

        for i in range(n-2, -1, -1):
            suf[i]=max(suf[i+1], height[i])


        res=0
        for i in range(n):
            if height[i]<suf[i] and height[i]<pre[i]:
                res+=min(suf[i], pre[i])-height[i]
        return res






        