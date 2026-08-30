class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def solve(i, j):
            if i>=len(s):
                return True

            if j>=len(t):
                return False

            if s[i]==t[j]:
                return solve(i+1, j+1)

            else:
                return solve(i, j+1)

            
        return solve(0, 0)
       
            
        