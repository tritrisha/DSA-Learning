class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        k=len(s)-1
        i=0
        while i<k:
            if s[i]==s[k]:
                k-=1
                i+=1
            else:
                return ispali(i+1, k) or ispali(i, k-1)

        return True

        

            


        