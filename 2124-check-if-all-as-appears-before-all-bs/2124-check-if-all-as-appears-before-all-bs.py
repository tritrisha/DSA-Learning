class Solution:
    def checkString(self, s: str) -> bool:
        b=0
        for i in range(len(s)):
            if s[i]=='a' and b==1:
                return False
            if s[i]=='b':
                b=1


        return True

        