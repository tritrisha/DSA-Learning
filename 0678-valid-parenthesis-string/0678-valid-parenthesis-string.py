class Solution:
    def checkValidString(self, s: str) -> bool:

        @lru_cache(None)
        def dp(stac, x, o):
            if o<0:
                return False
            if x==len(stac):
                return o==0
            if stac[x]=='(':
                return dp(stac, x+1, o+1)

            if stac[x]==')':
                return dp(stac, x+1, o-1)

            if stac[x]=='*':
                return dp(stac, x+1, o+1) or dp(stac, x+1, o-1) or dp(stac, x+1, o)

        
    
        
        return dp(s, 0, 0)
        

                
        
                
        