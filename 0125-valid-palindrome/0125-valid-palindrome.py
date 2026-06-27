class Solution:
    def isPalindrome(self, s: str) -> bool:
        j=''
        for i in s:
            if i.isalpha() or i.isdigit():
                j+=i
        
        j=j.lower()
        if j==j[::-1]:
            return True
        return False


        